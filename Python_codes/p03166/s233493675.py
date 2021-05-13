import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
  x,y=map(int,input().split())
  d[x-1].append(y-1)

dp=[-1]*n

def rec(v):
  if dp[v]!=-1:
    return dp[v]
  res=0
  for nv in d[v]:
    res=max(res,rec(nv)+1)
  dp[v]=res
  return res

res=0
for v in range(n):
  res=max(res,rec(v))
print(res)