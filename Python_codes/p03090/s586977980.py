# -*- coding: utf-8 -*-
from sys import stdin
# import numpy as np
# import sys
# sys.setrecursionlimit(10**4)

def _li(): return list(map(int, stdin.readline().split()))
def _li_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def _lf(): return list(map(float, stdin.readline().split()))
def _ls(): return stdin.readline().split()
def _i(): return int(stdin.readline())
def _f(): return float(stdin.readline())
def _s(): return stdin.readline()[:-1]


N = _i()

groups = []
if N % 2 == 0:
    for i in range(1, N//2+1):
        groups.append([i, N-i+1])
else:
    for i in range(1, N//2+1):
        groups.append([i, N-i])
    groups.append([N])

ans = []
for i in range(len(groups)):
    for j in range(i+1, len(groups)):
        if i == j:
            continue
        else:
            for g1 in groups[i]:
                for g2 in groups[j]:
                    ans.append([g1, g2])

print(len(ans))
for a in ans:
    print(a[0], a[1])
