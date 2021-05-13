import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b, c = list(map(int, sys.stdin.readline().split()))
    print('YES' if b - a == c - b else 'NO')


if __name__ == '__main__':
    main()
