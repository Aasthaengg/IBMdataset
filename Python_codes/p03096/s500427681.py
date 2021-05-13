# -*- coding: utf-8 -*-
from bisect import bisect, bisect_left
from collections import defaultdict

def inpl(): return list(map(int, input().split()))
MOD = 10**9 + 7
N = int(input())
C = [-1]
for i in range(N):
    c = int(input())
    if c != C[-1]:
        C.append(c)
C = C[1:]
N = len(C)
DP = [1]*N

ixs = defaultdict(lambda: [-1])
ixs[C[0]].append(0)

for i, c in enumerate(C[1:], start=1):
    l = ixs[c][bisect_left(ixs[c], i) - 1]
    if l != -1:
        DP[i] = (DP[i-1] + DP[l])%(MOD)
    else:
        DP[i] = DP[i-1]
    ixs[c].append(i)
print(DP[-1])
