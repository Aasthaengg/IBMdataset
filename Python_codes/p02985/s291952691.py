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
nb = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, k = ns()
    e = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = ns()
        a, b = a - 1, b - 1
        e[a].append(b)
        e[b].append(a)

    table = [True for _ in range(n)]
    perm = [1]
    for i in range(k - 2, -1, -1):
        perm.append(perm[-1] * i % MOD)

    table[0] = False
    que = collections.deque(e[0])
    ans = k
    for i in range(len(e[0])):
        table[e[0][i]] = False
        ans *= k - i - 1
        ans %= MOD

    while len(que) > 0:
        for _ in range(len(que)):
            q = que.popleft()
            cnt = 0
            for i in range(len(e[q])):
                tmp = e[q][i]
                if table[tmp]:
                    table[tmp] = False
                    cnt += 1
                    que.appendleft(tmp)
            ans *= perm[min(len(perm) - 1, cnt)]
            ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
