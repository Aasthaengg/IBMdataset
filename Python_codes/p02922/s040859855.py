import sys
import math
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    A, B = map(int, input().split())

    a = math.ceil((B-1)/(A-1))
    print(a)


if __name__ == "__main__":
    main()
