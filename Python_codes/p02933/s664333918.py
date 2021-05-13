import sys
import os

def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a = int(sys.stdin.buffer.readline().decode().rstrip())
    s = sys.stdin.buffer.readline().decode().rstrip()

    if a >= 3200:
        print(s)
    else:
        print("red")

if __name__ == '__main__':
    main()