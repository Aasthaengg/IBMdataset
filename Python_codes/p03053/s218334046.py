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
    h, w = ns()
    table = [list(input()) for _ in range(h)]
    not_visited = [[True for _ in range(w)] for __ in range(h)]
    dist = [[INF for _ in range(w)] for __ in range(h)]

    que = collections.deque()
    for hi in range(h):
        for wi in range(w):
            if table[hi][wi] == "#":
                not_visited[hi][wi] = False
                dist[hi][wi] = 0
                que.append([hi, wi])

    nxt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cnt = -1
    ans = 0
    while len(que):
        cnt += 1
        for i in range(len(que)):
            hi, wi = que.popleft()
            for yi, xi in nxt:
                th = hi + yi
                tw = wi + xi
                if -1 < th < h and -1 < tw < w:
                    if not_visited[th][tw]:
                        not_visited[th][tw] = False
                        dist[th][tw] = min(dist[th][tw], dist[hi][wi] + 1)
                        que.append([th, tw])

    print(cnt)


if __name__ == '__main__':
    main()
