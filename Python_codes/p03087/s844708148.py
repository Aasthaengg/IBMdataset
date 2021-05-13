n,q=map(int,input().split())
t=input()

a=[0]*n
from collections import defaultdict
tail=defaultdict(int)
for i in range(n-1):
    if t[i]=="A"and t[i+1]=="C":
        a[i+1]+=1
        tail[i]+=1
from itertools import accumulate
a=list(accumulate(a))
for _ in range(q):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    if l==0:print(a[r])
    else:
        print(a[r]-a[l-1]-tail[l-1])