import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.readline().split()))
    print(A+B if A+B < 10 else 'error')


if __name__ == '__main__':
    main()
