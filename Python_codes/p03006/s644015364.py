from collections import *
(n,),*p=[[*map(int,i.split())] for i in open(0)]
d=defaultdict(int)
for x, y in p:
    for a, b in p:
        d[(x-a, y-b)]+=(x,y)!=(a,b)
print(n-max(d.values()))
