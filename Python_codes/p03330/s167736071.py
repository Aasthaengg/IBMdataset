import itertools
import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


# 色のパターン 30*29*28 == 24360
# 全部試すだけ

N, C = list(map(int, sys.stdin.buffer.readline().split()))
D = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(C)]
S = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

D = np.array(D, dtype=int)
S = np.array(S, dtype=int) - 1

md = np.zeros((N, N), dtype=int)
md += np.arange(N, dtype=int)
md += np.arange(N, dtype=int)[:, None]
md %= 3

# s += D[S[md == 0], colors[0]].sum()
# s += D[S[md == 1], colors[1]].sum()
# s += D[S[md == 2], colors[2]].sum()

# costs[d][c]: md == d の場所を c に変えるときのコスト
costs = [[0] * C for _ in range(3)]
for d in range(3):
    for c in range(C):
        # md == d の場所を c に変えるときのコスト
        costs[d][c] = D[S[md == d], c].sum()

ans = INF
for colors in itertools.permutations(range(C), r=3):
    ans = min(ans, costs[0][colors[0]] + costs[1][colors[1]] + costs[2][colors[2]])
print(ans)
