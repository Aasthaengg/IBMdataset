import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, t = list(map(int, sys.stdin.buffer.readline().decode().split()))
    print(max(0,X-t))


if __name__ == '__main__':
    main()
