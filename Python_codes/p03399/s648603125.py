import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b, c, d = [int(sys.stdin.readline().rstrip()) for _ in range(4)]
    print(min(a, b) + min(c, d))


if __name__ == '__main__':
    main()
