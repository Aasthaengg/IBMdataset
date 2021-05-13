from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from bisect import bisect
from itertools import accumulate

n,x=nii()
a=lnii()
a.sort()

b=list(accumulate(a))

if b[-1]<x:
  print(n-1)
else:
  inx=bisect(b,x)
  print(inx)