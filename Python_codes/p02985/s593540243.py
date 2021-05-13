#!/usr/bin/env python3
#ABC133 E

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

n,k = LI()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

lst = [-1]*n
lst[0] = k
que = deque()
que.append(0)
while que:
    v = que.popleft()
    if v == 0:
        cnt = 1
    else:
        cnt = 2
    for u in graph[v]:
        if lst[u] < 0:
            que.append(u)
            lst[u] = k - cnt
            cnt += 1
ans = 1
for i in lst:
    ans *= i
    ans %= mod
print(ans)