import sys
import os

OK = 'APPROVED'
NG = 'DENIED'


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.buffer.readline().split()))

    print('Yay!' if A + B <= 16 and A <= 8 and B <= 8 else ':(')


if __name__ == '__main__':
    main()
