import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *
from fractions import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
S = list(map(int, input()))

X = []
for c in S:
    if len(X) >= 1 and X[-1][0] == c:
        X[-1][1] += 1
    else:
        X.append([c, 1])

sm = [0] * (len(X) + 1)
for i in range(len(X)):
    sm[i + 1] = sm[i] + X[i][1]

ans = 0
for i in range(len(X)):
    if X[i][0] == 0:
        # X[i] ... X[i + (K - 1) * 2 + 1]
        ans = max(ans, sm[min(i + (K - 1) * 2 + 2, len(X))] - sm[i])
        pass
    else:
        # X[i] ... X[i + K * 2]
        ans = max(ans, sm[min(i + K * 2 + 1, len(X))] - sm[i])
print(ans)
