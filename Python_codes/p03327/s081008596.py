import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = int(sys.stdin.buffer.readline().rstrip())
    print('ABC' if N <= 999 else 'ABD')


if __name__ == '__main__':
    main()
