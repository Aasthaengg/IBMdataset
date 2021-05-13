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
    n = ni()
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = ns()
        a -= 1
        b -= 1
        edge[a].append((b, c))
        edge[b].append((a, c))

    dist_table = [-1 for _ in range(n)]

    def dfs(node, dist):
        for t, cost in edge[node]:
            if dist_table[t] == -1:
                dist_table[t] = dist + cost
                dfs(t, dist_table[t])
        return

    q, k = ns()
    k -= 1
    dist_table[k] = 0
    dfs(k, 0)

    for _ in range(q):
        x, y = ns()
        print(dist_table[x - 1] + dist_table[y - 1])


if __name__ == '__main__':
    main()
