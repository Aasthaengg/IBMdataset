import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.buffer.readline().split()))
    print(A if A <= B else A-1)


if __name__ == '__main__':
    main()
