from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

N = int(input())

al = [[] for i in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    al[a].append((b,c))
    al[b].append((a,c))


seen = [0 for i in range(N+1)]
ans = [0 for i in range(N+1)]

def bfs(u):
    stack = deque([u])
    seen[u] = 1
    ans[u] = 0

    while len(stack) > 0:
        v = stack.popleft()

        for w in al[v]:
            if seen[w[0]] == 0:
                stack.append(w[0])
                if w[1] % 2 == 0:
                    ans[w[0]] = ans[v]
                else:
                    ans[w[0]] = 1 - ans[v]
                seen[w[0]] = 1

bfs(1)

for i in range(1,N+1):
    print(ans[i])