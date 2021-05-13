import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C, D = list(map(int, sys.stdin.buffer.readline().split()))
    print('Left' if A + B > C + D else 'Balanced' if A + B == C + D else 'Right')


if __name__ == '__main__':
    main()
