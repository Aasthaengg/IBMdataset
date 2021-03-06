# import bisect
from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, ipti().split()))
    node_next = [set() for _ in range(n)]

    for i in range(m):
        u, v = list(map(int, ipti().split()))
        node_next[u - 1].add(v - 1)

    s, t = list(map(int, ipti().split()))
    s, t = s - 1, t - 1

    dist = [[INF] * n for _ in range(3)]
    dist[0][s] = 0

    que = deque()
    que.append((0, s))

    while que:
        cstate, cnode = que.popleft()
        d = dist[cstate][cnode]
        nstate = (cstate + 1) % 3
        for nnode in node_next[cnode]:
            if dist[nstate][nnode] == INF:
                dist[nstate][nnode] = d + 1
                que.append((nstate, nnode))

    if dist[0][t] != INF:
        print(dist[0][t] // 3)
    else:
        print(-1)


if __name__ == '__main__':
    main()
