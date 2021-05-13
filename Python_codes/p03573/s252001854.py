import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C = list(map(int, sys.stdin.buffer.readline().decode().split()))
    print(C if A == B else A if B == C else B)


if __name__ == '__main__':
    main()
