#!/usr/bin/python3

from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def main():
    A, B = map(int, input().split())

    ans = [[""] * 100 for _ in range(100)]
    for y in range(100):
        for x in range(100):
            if x < 50:
                ans[y][x] = "#"
            else:
                ans[y][x] = "."
    A -= 1
    B -= 1
    for y in range(1, 100, 2):
        for x in range(1, 100, 2):
            if 10 < x < 40:
                if A > 0:
                    ans[y][x] = "."
                    A -= 1
            if 60 < x < 90:
                if B > 0:
                    ans[y][x] = "#"
                    B -= 1

    print(100, 100)
    for line in ans:
        print("".join(line))


if __name__ == '__main__':
    main()
