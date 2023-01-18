import keyboard
import winsound
import threading
def Press(x:keyboard.KeyboardEvent):
    print(x)
    if str(x.event_type)=="down":
        if x.name in "qwertyuiopasdfghjklzxcvbnm0123456789":
            threading.Thread(target=play(f"keysound/{x.name}.wav")).start()
def play(wav_path):
    winsound.PlaySound(wav_path, winsound.SND_ASYNC)
if __name__ == '__main__':
    keyboard.hook(Press)
    keyboard.wait()



