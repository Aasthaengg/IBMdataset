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
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n, m = ns()
    e = [[] for _ in range(n)]
    for _ in range(m):
        a, b = ns()
        e[a - 1].append(b - 1)

    res = [-1 for _ in range(n)]

    def dfs(ti):
        tmp = 0
        for vi in e[ti]:
            if res[vi] != -1:
                tmp = max(tmp, res[vi] + 1)
            else:
                tmp = max(tmp, dfs(vi) + 1)
        res[ti] = tmp
        return tmp

    ans = 0
    for i in range(n):
        if res[i] == -1:
            ans = max(ans, dfs(i))

    print(ans)


if __name__ == '__main__':
    main()
