n,k=map(int,input().split())
a=list(map(int,input().split()))
a=list(map(lambda x:x-1 ,a))

s=[0]
for i in range(n):
    s.append(s[-1]+a[i])
s=list(map(lambda x:x%k,s))
from collections import defaultdict
d=defaultdict(int)
d[0]=1
ans=0

for i in range(1,n+1):
    if i>=k:
        d[s[i-k]]-=1
    ans+=d[s[i]]
    d[s[i]]+=1
print(ans)
