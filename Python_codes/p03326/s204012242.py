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


# プラスマイナスどっちにするかを8パターン全部試す

N, M = list(map(int, sys.stdin.buffer.readline().split()))
XYZ = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]
XYZ = np.array(XYZ, dtype=int)

ans = -INF
for sgn in itertools.product([-1, 1], repeat=3):
    H = np.dot(XYZ, sgn)
    H = np.msort(H)[::-1]
    ans = max(ans, H[:M].sum())
print(ans)
