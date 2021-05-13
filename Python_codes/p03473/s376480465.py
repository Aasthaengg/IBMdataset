import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    M = int(sys.stdin.readline().rstrip())
    print(24+(24-M))


if __name__ == '__main__':
    main()
