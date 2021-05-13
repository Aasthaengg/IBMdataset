import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, A = list(map(int, sys.stdin.buffer.readline().split()))
    print(0 if X < A else 10)


if __name__ == '__main__':
    main()
