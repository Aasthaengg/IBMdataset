from collections import *

N,W=map(int,input().split())
d=defaultdict(int)
d[0]=0
for i in range(N):
    w,v=map(int,input().split())
    for p,q in d.copy().items():
        if p+w<=W:
            d[p+w]=max(d[p+w],q+v)
print(max(d.values()))