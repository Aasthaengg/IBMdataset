from collections import defaultdict
import itertools


n,k= map(int, input().split())
a= list(map(int, input().split()))
a=[0]+list(itertools.accumulate(a))
b=[0]*(n+1)
for i,x in enumerate(a):
    b[i]=(x-i)%k
d=defaultdict(int)
ans=0
for i in range(n+1):
    if i>=k:
        d[b[i-k]]-=1
    ans+=d[b[i]]
    d[b[i]]+=1
print(ans)