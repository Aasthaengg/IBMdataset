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
    d = []
    for _ in range(h):
        tmp = list(input())
        d.extend(tmp)

    c = collections.Counter(d)

    flg1 = w % 2
    flg2 = h % 2
    even_pocket = h * flg1 + w * flg2 - flg1 * flg2 * 2
    odd_pocket = flg1 * flg2

    ans = True
    for k, v in c.items():
        even_pocket -= ((v % 4) // 2) * 2
        odd_pocket -= v % 2
        if even_pocket < 0 or odd_pocket < 0:
            ans = False
            break

    print("Yes" if ans else "No")


if __name__ == '__main__':
    main()
