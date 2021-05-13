from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque

n,m = [int(x) for x in stdin.readline().rstrip().split()]

d = {}
for i in range(m):
    a,b = [int(x) for x in stdin.readline().rstrip().split()]

    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)

    if b not in d:
        d[b] = [a]
    else:
        d[b].append(a)

sol = {}

m = [1]
while True:
    next_m = []
    for mm in m:
        b = d[mm]
        for bb in b:
            if bb not in sol:
                sol[bb] = mm
                next_m.append(bb)

    if len(next_m) == 0: break
    m = next_m

sol = sorted(sol.items())

print("Yes")
for v in sol[1:]:
    print(v[1])