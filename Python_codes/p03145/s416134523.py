import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    ab, bc, ca = map(int, sys.stdin.readline().split())

    print(int(ab*bc/2))


if __name__ == '__main__':
    main()
