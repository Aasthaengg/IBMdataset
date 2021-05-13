import sys
import os

OK = 'APPROVED'
NG = 'DENIED'


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C, D = list(map(int, sys.stdin.buffer.readline().split()))

    print('Yes' if abs(A - B) <= D and abs(B - C) <= D or abs(A - C) <= D else 'No')


if __name__ == '__main__':
    main()
