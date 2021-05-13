import sys
import math
import collections
import bisect
import copy
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    p = [ni() - 1 for _ in range(n)]

    table = [0] * n

    maxnum = 0
    for i in range(n):
        idx = p[i]
        if idx == 0:
            table[idx] = 1
        else:
            table[idx] = table[idx - 1] + 1
        maxnum = max(maxnum, table[idx])

    print(n - maxnum)


if __name__ == '__main__':
    main()
