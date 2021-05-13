import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
from itertools import *
from copy import *

N, C = map(int, input().split())
f1 = [list(map(int, input().split())) for i in range(N)]
f2 = deepcopy(f1)[::-1]
for i in range(N-1):
    f1[i+1][1] += f1[i][1]
    f2[i+1][1] += f2[i][1]
f1 = [[0, 0, 0]] + [(v-x, x, i) for i, (x, v) in enumerate(f1, 1)]
f2 = [[0, 0, 0]] + [(v-C+x, C-x, i) for i, (x, v) in enumerate(f2, 1)]
g1 = [0] * (N+1)
g2 = [0] * (N+1)
for i in range(1, N+1):
    g1[i] = max(f1[i][0], g1[i-1])
    g2[i] = max(f2[i][0], g2[i-1])
ans = 0
for i in range(N+1):
    ans = max(ans, f1[i][0]+g2[N-i]-f1[i][1], f2[i][0]+g1[N-i]-f2[i][1])
print(ans)
