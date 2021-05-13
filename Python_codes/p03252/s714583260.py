import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

S = input()
T = input()

x = defaultdict(list)
y = defaultdict(list)

for i, t in enumerate(T):
    x[t].append(S[i])

for i, s in enumerate(S):
    y[s].append(T[i])

ok = True
for k, v in x.items():
    a = v[0]
    for c in v:
        if c != a:
            ok = False
            break

for k, v in y.items():
    a = v[0]
    for c in v:
        if c != a:
            ok = False
            break

if ok:
    print("Yes")
else:
    print("No")
