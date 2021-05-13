import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = int(sys.stdin.buffer.readline().rstrip())
    print('AGC' if N >= 2800 else 'ARC' if N >= 1200 else 'ABC')


if __name__ == '__main__':
    main()
