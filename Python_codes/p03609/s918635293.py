import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, t = list(map(int, sys.stdin.readline().split()))
    print(X-t if X - t >= 0 else 0)


if __name__ == '__main__':
    main()
