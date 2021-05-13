from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from heapq import *

n,m=nii()
a=lnii()
a=[-i for i in a]
a.sort(reverse=True)

heapify(a)

for i in range(m):
  x=heappop(a)
  x*=-1
  x//=2
  heappush(a,-x)

print(-sum(a))