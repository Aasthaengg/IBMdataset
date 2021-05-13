n,k=map(int,input().split())
a=list(map(int,input().split()))
a=list(map(lambda x:x-1 ,a))

if k==1:
    print(0)
    exit()
s=[0]
for i in range(n):
    s.append(s[-1]+a[i])
s=list(map(lambda x:x%k,s))
from collections import defaultdict
d=defaultdict(int)
d[0]=1
ans=0

for i in range(1,n+1):
    ans+=d[s[i]]
    d[s[i]]+=1
    if i>=k-1:
        d[s[i-k+1]]-=1
print(ans)
