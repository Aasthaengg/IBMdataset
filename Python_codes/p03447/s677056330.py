import sys
from math import sqrt
from collections import Counter

input = sys.stdin.readline


def I():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    x = I()
    a = I()
    b = I()

    r = x - a
    while r >= b:
        r -= b
    print(r)
    pass


if __name__ == "__main__":
    main()
