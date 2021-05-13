import sys
from math import sqrt
from collections import Counter

input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    x, y = MI()

    c = 0
    while x <= y:
        c += 1
        x *= 2

    print(c)
    pass


if __name__ == "__main__":
    main()
