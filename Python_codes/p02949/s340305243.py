#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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

n, m, p = LI()
abc = [LI() for _ in range(m)]
edges = [[] for _ in range(n)]
inv_edges = [[] for _ in range(n)]
for a, b, c in abc:
    edges[a-1].append((b-1, c))
    inv_edges[b-1].append(a-1)

visited = [False] * n
stack = [n-1]
while stack:
    v = stack.pop()
    visited[v] = True
    for u in inv_edges[v]:
        if visited[u]:
            continue
        stack.append(u)

dp = [-float('inf')] * n
dp[0] = 0
tmp = -1
for _ in range(n+1):
    flag = False
    for v in range(n):
        score = dp[v]
        for u, c in edges[v]:
            if dp[u] < score + c - p and visited[u]:
                dp[u] = score + c - p
                flag = True
if flag:
    print(-1)
else:
    print(max(0, dp[n-1]))