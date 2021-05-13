import math
import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())

cnt = math.ceil(math.sqrt(N * 2))
if cnt * (cnt - 1) != N * 2:
    print('No')
    exit()

ans = np.zeros((cnt, cnt - 1), dtype=int)
ans[np.triu_indices(cnt - 1)] = np.arange(1, N + 1)
ans[1:].T[np.triu_indices(cnt - 1)] = np.arange(1, N + 1)
print('Yes')
print(cnt)
for r in ans:
    print(cnt - 1, *r)
