import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,C = map(int,(input().split()))
D = [[] for _ in range(C)]
c = [[] for _ in range(N)]
for i in range(C):
    D[i] = list(map(int,(input().split())))
for i in range(N):
    c[i] = list(map(int,(input().split())))

r0 = []
r1 = []
r2 = []
for i in range(N):
    for j in range(N):
        if (i+j)%3 == 0:
            r0.append(c[i][j])
        elif (i+j)%3 == 1:
            r1.append(c[i][j])
        else:
            r2.append(c[i][j])

d0 = [[]]*C
d1 = [[]]*C
d2 = [[]]*C
for color in range(C):
    s = 0
    for i in range(len(r0)):
        s += D[r0[i]-1][color]
    d0[color] = (s,color)
for color in range(C):
    s = 0
    for i in range(len(r1)):
        s += D[r1[i]-1][color]
    d1[color] = (s,color)
for color in range(C):
    s = 0
    for i in range(len(r2)):
        s += D[r2[i]-1][color]
    d2[color] = (s,color)

d0.sort()
d1.sort()
d2.sort()

ans = float("inf")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if d0[i][1] != d1[j][1] and d0[i][1] != d2[k][1] and d1[j][1] != d2[k][1]:
                ans = min(ans,d0[i][0]+d1[j][0]+d2[k][0])
print(ans)