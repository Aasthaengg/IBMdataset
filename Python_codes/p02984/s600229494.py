import math
import itertools
import collections
import bisect
import heapq

def IN(): return int(input())
def sIN(): return input()
def MAP(): return map(int,input().split())
def LMAP(): return list(map(int,input().split()))
def TATE(n): return [input() for i in range(n)]

n = IN()
a = LMAP()
ans = []
yama1 = 0

for i in range(n):
  if i%2 == 0:
    yama1 += a[i]
  else:
    yama1 += a[i]*(-1)
    
ans.append(yama1)

for i in range(1,n):
  ans.append(2*a[i-1] - ans[i-1])
  
print(*ans)