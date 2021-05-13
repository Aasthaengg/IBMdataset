import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    h, w = ns()
    mat = [na() for _ in range(h)]

    n = 0
    ans = []
    for y in range(h):
        for x in range(w - 1):
            if mat[y][x] % 2:
                mat[y][x] -= 1
                mat[y][x + 1] += 1
                ans.append((y + 1, x + 1, y + 1, x + 1 + 1))
                n += 1

    for y in range(h - 1):
        if mat[y][w - 1] % 2:
            mat[y][w - 1] -= 1
            mat[y + 1][w - 1] += 1
            ans.append((y + 1, w, y + 1 + 1, w))
            n += 1

    print(n)
    for item in ans:
        print(*item, sep=" ")


if __name__ == '__main__':
    main()
