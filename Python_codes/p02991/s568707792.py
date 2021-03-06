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
    n, m = ns()
    e = [[] for _ in range(n)]
    for _ in range(m):
        a, b = ns()
        a, b = a - 1, b - 1
        e[a].append(b)

    s, t = ns()
    s, t = s - 1, t - 1

    visited = [[True] * 3 for _ in range(n)]

    que = collections.deque()
    que.append([0, s])
    visited[s][0] = False
    cnt = 0
    ans = -1
    flg = True

    while que and flg:
        cnt += 1
        for _ in range(len(que)):
            i, q = que.popleft()
            for ei in e[q]:
                tmp = (i + 1) % 3
                if tmp == 0 and ei == t:
                    ans = cnt // 3
                    flg = False
                    break
                elif visited[ei][tmp]:
                    visited[ei][tmp] = False
                    que.append([tmp, ei])

    print(ans)


if __name__ == '__main__':
    main()
