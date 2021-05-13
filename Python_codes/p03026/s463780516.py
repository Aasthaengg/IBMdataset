from itertools import*
import math
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

N = int(input())
D =[[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    D[a].append(b)
    D[b].append(a)

c = sorted(list(map(int,input().split())))
vcost = [-1]*(N+1)
vcost[1]=c.pop()
ans = 0
def dfs(i):
    global ans
    for j in D[i]:
        if vcost[j]==-1:
            vcost[j]=c.pop()
            ans += vcost[j]
            dfs(j)
dfs(1)
print(ans)
print(*vcost[1:])