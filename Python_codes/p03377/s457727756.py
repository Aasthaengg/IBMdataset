import sys
import os

OK = 'APPROVED'
NG = 'DENIED'


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, X = list(map(int, sys.stdin.buffer.readline().split()))

    print('YES' if A <= X and X - A <= B else 'NO')


if __name__ == '__main__':
    main()
