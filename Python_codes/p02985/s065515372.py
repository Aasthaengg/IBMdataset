# import bisect
from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class Node:

    def __init__(self, nid):
        self.node_id = nid
        self.color = -1
        self.next = []


def main():
    n, k = list(map(int, readline().split()))

    nodes = [Node(i) for i in range(n)]

    for i in range(n - 1):
        a, b = list(map(int, readline().split()))
        a, b = a - 1, b - 1
        nodes[a].next.append(b)
        nodes[b].next.append(a)

    que = deque()
    que.append((0, 0, 0))

    while que:
        current_id, cn_1, cn_2 = que.popleft()

        cl = k - cn_1 - cn_2

        if cl <= 0:
            print(0)
            sys.exit()

        nodes[current_id].color = cl

        for nid in nodes[current_id].next:
            if nodes[nid].color == -1:
                cn_1 += 1
                que.append((nid, 1, cn_1 - 1))

    ans = 1
    for i in range(n):
        ans *= nodes[i].color
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
