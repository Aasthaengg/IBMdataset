import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a = int(sys.stdin.buffer.readline().rstrip())
    s = sys.stdin.buffer.readline().decode().rstrip()
    print(s if a >= 3200 else 'red')


if __name__ == '__main__':
    main()
