n,m=map(int,input().split())
l=[0]+list(map(int,input().split()))
from itertools import accumulate
l=list(accumulate(l))
l=[i%m for i in l]
import collections
c=collections.Counter(l)
ans=0
for i in c.values():
    ans+=i*(i-1)//2
print(ans)