import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b = map(str, sys.stdin.readline().split())

    print("DH"[a == b])


if __name__ == '__main__':
    main()
