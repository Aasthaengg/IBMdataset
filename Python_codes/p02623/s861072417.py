import itertools
import bisect
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
a=list(itertools.accumulate(a))
b=list(itertools.accumulate(b))
ans=0
for i in range(m+1):
  x=k-b[i]
  y=bisect.bisect_right(a,x)
  z=i+y
  if x<0:
      z=0
  ans=max(ans,z)
print(ans)