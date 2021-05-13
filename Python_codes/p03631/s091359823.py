import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b, c = str(sys.stdin.readline().rstrip())
    print("Yes" if a == c else "No")


if __name__ == '__main__':
    main()
