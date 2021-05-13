n,T=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*n
mn=10**18
for i in range(1,n):
  mn=min(mn,a[i-1])
  b[i]=a[i]-mn
# print(b)
from collections import Counter
c=Counter(b)
ans=0
for k,v in sorted(c.items(),reverse=1):
  ans+=v
  break
print(ans)