import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===

def main():
    x, y, z, w = ns()
    a = na()
    b = na()
    c = na()

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    ans = []
    for ai in a:
        for bi in b:
            ans.append(ai + bi)

    ans.sort(reverse=True)
    ans = ans[:3010]

    res = []
    for ci in c:
        for i in range(len(ans)):
            res.append(ci + ans[i])
    res.sort(reverse=True)

    for i in range(w):
        print(res[i])


if __name__ == '__main__':
    main()
