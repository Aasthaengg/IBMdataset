#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

N, M = map(int, input().split())
# PY = [list(map(int, input().split())) for _ in range(M)]
PY = []
for i in range(M):
    P, Y = map(int, input().split())
    PY.append((i, P, Y))

PYs = sorted(PY, key=lambda x:(x[1], x[2]))
# print(PYs)

d = defaultdict(int)
ress = []
for py in PYs:
    i, p, y = py
    ress.append((i, p, d[p]+1))
    d[p] += 1

ress.sort(key=lambda x: x[0])
for res in ress:
    i, p, o = res
    print(str(p).zfill(6)+str(o).zfill(6))
