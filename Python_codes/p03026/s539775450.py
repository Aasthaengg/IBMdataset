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
    n = ni()
    e = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = ns()
        a, b = a - 1, b - 1
        e[a].append(b)
        e[b].append(a)

    c = na()
    c.sort(reverse=True)
    cost = collections.deque(c)

    notvisited = [True for _ in range(n)]
    ans = [-1 for _ in range(n)]

    que = collections.deque(e[0])
    notvisited[0] = False
    ans[0] = cost.popleft()

    while que:
        for _ in range(len(que)):
            q = que.popleft()
            if notvisited[q]:
                ans[q] = cost.popleft()
                notvisited[q] = False
                for ei in e[q]:
                    que.append(ei)

    res = 0
    for i in range(n):
        for ei in e[i]:
            if i < ei:
                res += min(ans[i], ans[ei])

    print(res)
    print(*ans, sep=" ")


if __name__ == '__main__':
    main()
