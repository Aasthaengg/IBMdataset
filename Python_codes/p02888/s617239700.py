n=int(input())
l=list(map(int,input().split()))
from bisect import bisect_left
l.sort()
ans=0
for i in range(n-2):
  for j in range(i+1,n-1):
    t=l[i]+l[j]
    idx=bisect_left(l,t)
    ans+=max(idx-j-1,0)
print(ans)
