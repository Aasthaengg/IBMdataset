import sys
import os

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A = ii()
    B = ii()
    print('GREATER' if A > B else 'LESS' if A < B else 'EQUAL')


if __name__ == '__main__':
    main()
