import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A = int(sys.stdin.buffer.readline().rstrip())
    B = int(sys.stdin.buffer.readline().rstrip())
    print('GREATER' if A > B else 'LESS' if A < B else 'EQUAL')


if __name__ == '__main__':
    main()
