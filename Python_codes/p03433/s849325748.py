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
    n = I()
    a = I()

    if n % 500 <= a:
        print("Yes")
    else:
        print("No")

    pass


if __name__ == "__main__":
    main()
