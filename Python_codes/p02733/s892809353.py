
import heapq
from collections import defaultdict, deque
# from math import ceil, factorial, gcd
from itertools import accumulate, permutations
import sys
import bisect


sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
msi = lambda: map(str, input().split())
lmii = lambda: list(map(int, input().split()))
lmsi = lambda: list(map(str, input().split()))
smii = lambda: sorted(map(int, input().split()))
# ----------

H, W, K = mii()
S = []
for i in range(H):
    S.append(si())

ans = INF
for div in range(1<<(H-1)):
    id = [0] * H
    g = 0
    for i in range(H):
        id[i] = g
        if div >> i & 1:
            g += 1

    c = [[0] * W for _ in range(g+1)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '1':
                c[id[i]][j] += 1

    now = defaultdict(int)

    def add(j):
        for i in range(g+1):
            now[i] += c[i][j]
        for i in range(g+1):
            if now[i] > K:
                return False
        return True

    num = g
    for j in range(W):
        if not add(j):
            num += 1
            now = defaultdict(int)
            if not add(j):
                num = INF
                break

    ans = min(ans, num)

print(ans)

