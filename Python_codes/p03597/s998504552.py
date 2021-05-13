import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = int(sys.stdin.readline().rstrip())
    A = int(sys.stdin.readline().rstrip())
    print(N * N - A)


if __name__ == '__main__':
    main()
