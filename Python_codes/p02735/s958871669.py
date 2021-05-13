import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 10
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    h, w = ns()
    mat = [list(input()) for _ in range(h)]

    ans_mat = [[INF for _ in range(w)] for _ in range(h)]
    if mat[0][0] == "#":
        ans_mat[0][0] = 1
    else:
        ans_mat[0][0] = 0

    for y in range(h):
        for x in range(w):
            if x + 1 < w:
                if mat[y][x] != mat[y][x + 1]:
                    ans_mat[y][x + 1] = min(ans_mat[y][x + 1], ans_mat[y][x] + 1)
                else:
                    ans_mat[y][x + 1] = min(ans_mat[y][x + 1], ans_mat[y][x])

            if y + 1 < h:
                if mat[y][x] != mat[y + 1][x]:
                    ans_mat[y + 1][x] = min(ans_mat[y + 1][x], ans_mat[y][x] + 1)
                else:
                    ans_mat[y + 1][x] = min(ans_mat[y + 1][x], ans_mat[y][x])

    tmp = ans_mat[h - 1][w - 1]
    print(tmp - tmp // 2)


if __name__ == '__main__':
    main()
