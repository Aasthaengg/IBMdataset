import sys

sys.setrecursionlimit(10000000)
import os
import math
import bisect
import collections
import itertools
import heapq
import re
import queue
from decimal import Decimal

# import fractions

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def dfs(s, graph, bridge, visit):
    visit[s] = True
    for next in graph[s]:
        if not bridge[s][next]: continue
        if visit[next]: continue
        dfs(next, graph, bridge, visit)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, M = il()
    graph = {n: [] for n in range(N)}

    for _ in range(M):
        a, b = il()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    ret = 0
    bridge = {n: [True] * N for n in range(N)}
    searched = {n: [False] * N for n in range(N)}
    for i in range(N):
        for j in graph[i]:
            if searched[i][j]: continue
            searched[i][j],searched[j][i] = True, True
            visit = [False] * N
            bridge[i][j],bridge[j][i] = False, False
            dfs(0, graph, bridge, visit)
            if not all(visit): ret += 1
            bridge[i][j], bridge[j][i] = True, True
    print(ret)


if __name__ == '__main__':
    main()
