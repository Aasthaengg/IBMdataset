n,k=map(int,input().split())
a=list(map(lambda x:(int(x)-1)%k,input().split()))
a_=0
cs_a=[0]
for ai in a:
  a_+=ai
  a_%=k
  cs_a.append(a_)
ans=0
from collections import defaultdict
d=defaultdict(int)
for i in range(n+1):
  ans+=d[cs_a[i]]
  d[cs_a[i]]+=1
  if i>=k-1:
    d[cs_a[i-k+1]]-=1
print(ans)
