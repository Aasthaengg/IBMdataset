#!/usr/bin/env python3
#M-SOLUTIONS プロコンオープン D

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
cnt = [0]*n
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = LI()
    cnt[a-1] += 1
    cnt[b-1] += 1
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
c = LI()
m = sum(c) - max(c)
print(m)
d = [0]*n
for i in range(n):
    if cnt[i] == 1:
        d[i] = max(c)
        break
c.sort(reverse = True)
c = c[1:]
que = deque(c)
def dfs(x,p):
    for v in graph[x]:
        if v != p:
            if d[v] == 0:
                d[v] = que.popleft()
                dfs(v,x)
dfs(i,-1)
print(*d)
