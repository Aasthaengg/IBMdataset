import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    n, m = list(map(int, sys.stdin.readline().split()))
    print((n-1)*(m-1))


if __name__ == '__main__':
    main()
