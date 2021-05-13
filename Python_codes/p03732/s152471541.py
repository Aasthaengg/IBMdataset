import itertools
import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, W = list(map(int, sys.stdin.readline().split()))
Ws, Vs = list(zip(*[map(int, sys.stdin.readline().split()) for _ in range(N)]))

Ws = np.array(Ws)
Vs = np.array(Vs)

w1 = Ws[0]
ws = np.arange(4) + w1
v1s = Vs[Ws == ws[0]]
v2s = Vs[Ws == ws[1]]
v3s = Vs[Ws == ws[2]]
v4s = Vs[Ws == ws[3]]
v1s.sort()
v2s.sort()
v3s.sort()
v4s.sort()
v1s = np.concatenate([[0], v1s[::-1].cumsum()])
v2s = np.concatenate([[0], v2s[::-1].cumsum()])
v3s = np.concatenate([[0], v3s[::-1].cumsum()])
v4s = np.concatenate([[0], v4s[::-1].cumsum()])

counts = np.array(list(itertools.product(
    range(len(v1s)),
    range(len(v2s)),
    range(len(v3s)),
    range(len(v4s))
)))
counts = counts[np.dot(counts, ws) <= W]

sums = v1s[counts[:, 0]] + \
       v2s[counts[:, 1]] + \
       v3s[counts[:, 2]] + \
       v4s[counts[:, 3]]

print(sums.max())
