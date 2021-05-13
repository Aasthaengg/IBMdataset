import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, Y = list(map(str, sys.stdin.buffer.readline().decode().split()))
    print('>' if X>Y else '=' if X==Y else '<')


if __name__ == '__main__':
    main()
