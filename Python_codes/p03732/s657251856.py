n,W=map(int,input().split())
from collections import defaultdict
WD=[list(map(int,input().split())) for _ in range(n)]
d=defaultdict(int)
d[0]=0
for w,v in WD:
    for i ,j in d.copy().items():
        if i+w <=W:
            d[w+i]=max(d[w+i],j+v)

print(max(d.values()))