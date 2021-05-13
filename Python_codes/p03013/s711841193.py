import sys
from functools import lru_cache
sys.setrecursionlimit(10**9)
MOD=10**9+7
n,m=map(int,input().split())
a=set([int(input()) for _ in range(m)])
if n==1:
  print(1)
  exit()
if 1 in a and 2 in a:
  print(0)
  exit()
elif 1 in a:
  ans=[0,0,1]
elif 2 in a:
  ans=[0,1,0]
else:
  ans=[0,1,2]

@lru_cache(maxsize=None)
def cnt(x):
  if x<3:
    return ans[x]
  if x in a:
    return 0
  else:
    return (cnt(x-1)+cnt(x-2))%MOD

print(cnt(n))