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

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n, u, v = ns()
    edge = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = ns()
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    dist_takahashi = [-1] * n
    dist_aoki = [-1] * n

    def bfs(pos, dist):
        que = queue.Queue()
        que.put(pos)
        dist[pos] = 0

        while not que.empty():
            current = que.get()
            for e in edge[current]:
                if dist[e] == -1:
                    dist[e] = dist[current] + 1
                    que.put(e)

        return dist

    dist_takahashi = bfs(u - 1, dist_takahashi)
    dist_aoki = bfs(v - 1, dist_aoki)

    ans = 0
    for dt, da in zip(dist_takahashi, dist_aoki):
        if dt < da:
            ans = max(ans, da - 1)

    print(ans)


if __name__ == '__main__':
    main()
