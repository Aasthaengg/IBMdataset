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
    a, b, c, d = MI()

    l = a + b
    r = c + d
    if l > r:
        print("Left")
    elif l < r:
        print("Right")
    else:
        print("Balanced")
    pass


if __name__ == "__main__":
    main()
