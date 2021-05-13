import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10**9)
mod = 10**9+7
N,Q = I()
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = I()
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
ans = [0]*N
for _ in range(Q):
    p,x = I()
    ans[p-1] += x
que = [0]
visited = {0}
while que:
    p = []
    for i in que:
        for j in edge[i]:
            if j in visited:
                continue
            visited.add(j)
            ans[j] += ans[i]
            p.append(j)
    que = p
print(*ans)