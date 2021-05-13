import sys
import os
import math


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, D = list(map(int, sys.stdin.readline().split()))
    look = 2 * D + 1
    print(math.ceil(N / look))


if __name__ == '__main__':
    main()
