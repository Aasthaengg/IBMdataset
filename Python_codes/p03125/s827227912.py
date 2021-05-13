import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.buffer.readline().split()))
    print(B+A if B%A == 0 else B-A)


if __name__ == '__main__':
    main()
