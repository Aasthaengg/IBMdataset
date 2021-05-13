import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.buffer.readline().split()))
    print((A+B)%24)

if __name__ == '__main__':
    main()
