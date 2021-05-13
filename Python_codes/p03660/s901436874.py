#!/usr/bin/env python3
#ABC67 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

que = deque()
que.append((0,0))
c1 = [False]*n
dist1 = [float('inf')]*n
while que:
    d,v = que.popleft()
    dist1[v] = min(dist1[v],d)
    if not c1[v]:
        c1[v] = True
        for u in g[v]:
            que.append((d+1,u))
que = deque()
que.append((0,n-1))
c2 = [False]*n
dist2 = [float('inf')]*n
while que:
    d,v = que.popleft()
    dist2[v] = min(dist2[v],d)
    if not c2[v]:
        c2[v] = True
        for u in g[v]:
            que.append((d+1,u))

w,b = 0,0
for i in range(n):
    if dist1[i] <= dist2[i]:
        b += 1
    else:
        w += 1
if w < b:
    print('Fennec')
else:
    print('Snuke')
