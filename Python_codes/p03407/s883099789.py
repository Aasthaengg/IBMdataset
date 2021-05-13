import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C = list(map(int, sys.stdin.buffer.readline().split()))
    print('Yes' if A+B>=C else 'No')


if __name__ == '__main__':
    main()
