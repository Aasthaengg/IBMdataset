import sys
import os
import math


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.readline().split()))
    print(math.ceil((A+B)/2))

if __name__ == '__main__':
    main()
