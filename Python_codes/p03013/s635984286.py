import sys
from functools import lru_cache
sys.setrecursionlimit(10**9)
MOD=10**9+7
n,m=map(int,input().split())
a=set([int(input()) for _ in range(m)])
if 1 in a:
  ans=[1,0]
else:
  ans=[1,1]

@lru_cache(maxsize=None)
def cnt(x):
  if x<2:
    return ans[x]
  if x in a:
    return 0
  else:
    return (cnt(x-1)+cnt(x-2))%MOD

print(cnt(n))