import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b = list(map(int, sys.stdin.buffer.readline().split()))
    print((a-1)+int(a<=b))


if __name__ == '__main__':
    main()
