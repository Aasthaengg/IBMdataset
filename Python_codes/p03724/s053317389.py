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
    n, m = ns()
    table = [0 for _ in range(n)]

    for _ in range(m):
        a, b = ns()
        a -= 1
        b -= 1
        table[a] ^= 1
        table[b] ^= 1

    ans = max(table)

    print("NO" if ans else "YES")





if __name__ == '__main__':
    main()
