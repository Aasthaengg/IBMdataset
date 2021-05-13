from bisect import bisect_right
from numpy import cumsum
from sys import stdin
input=stdin.readline
n,m,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
b=list(map(int,input().split()))
a=cumsum(a)
b=cumsum(b)
ans=0
for i in range(len(a)):
  x=k-a[i]
  if x>=0:
    y=bisect_right(b,x)
    if ans<y+i:
      ans=y+i
  else:
    break
print(ans)