n,k=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
from itertools import accumulate
l=[0]+list(accumulate(a))
ll=[]
for i in range(n+1):
    ll.append((i-l[i])%k)
import collections
c=collections.Counter()
ans=0
for i in range(n+1):
    ans+=c[ll[i]]
    c[ll[i]]+=1
    if i>=k-1:
        c[ll[i-k+1]]-=1
print(ans)