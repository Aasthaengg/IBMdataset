import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C = list(map(int, sys.stdin.readline().split()))
    print(A*B//2)


if __name__ == '__main__':
    main()
