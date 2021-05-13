from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from bisect import bisect

n,x=nii()
a=lnii()
a.sort()

b=[0]
for i in range(1,n+1):
  b.append(a[i-1]+b[i-1])
b=b[1:]

if b[-1]<x:
  print(n-1)
else:
  inx=bisect(b,x)
  print(inx)