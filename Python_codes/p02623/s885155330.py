from itertools import accumulate
import bisect
n,m,k=map(int,input().split())
a=list(accumulate([0]+list(map(int,input().split()))))
b=list(accumulate(list(map(int,input().split()))))
ans=0
for i in range(n+1):
  if a[i]>k:break
  j=bisect.bisect_right(b,k-a[i])
  ans=max(i+j,ans)
print(ans)