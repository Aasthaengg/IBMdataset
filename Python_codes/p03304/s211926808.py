import sys
import math
import collections
import bisect
import copy

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
    n, m, d = ns()
    if d == 0:
        l = n
    else:
        l = 2 * (n - d)
    tmp = l * (m - 1) / pow(n, 2)
    print(tmp)


if __name__ == '__main__':
    main()
