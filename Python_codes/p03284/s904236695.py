import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, K = list(map(int, sys.stdin.buffer.readline().split()))
    print(int(N%K != 0))


if __name__ == '__main__':
    main()
