n,k=map(int,input().split())
from operator import itemgetter as it
l=sorted([list(map(int,input().split()))for i in range(n)],reverse=1,key=it(1))
from collections import defaultdict
c=defaultdict(int)
from heapq import heapify, heappop, heappush
now=[]
S=0
kind=0
for i in range(k):
    a,s=l[i]
    S+=s
    c[a]+=1
    if c[a]>1:heappush(now,(s,a))
    kind+=c[a]==1
ans=S+kind**2
for i in range(k,n):
    if not now:break
    x,y=l[i]
    if c[x]:continue
    s,a=heappop(now)
    c[x]+=1
    kind+=1
    S+=y-s
    ans=max(ans,S+kind**2)
print(ans)