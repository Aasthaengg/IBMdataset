from collections import defaultdict
from itertools import accumulate,product

N,W=map(int,input().split())
d={}
for i in range(N):
    w,v=map(int,input().split())
    if not i:
        for j in range(w,w+4):
            d[j]=[]
    d[w].append(v)

for i in d.keys():
    d[i].sort(reverse=True)
    *d[i],=accumulate([0]+d[i])

ans=0
i,j,k,l=d.keys()
for ai,bi in enumerate(d[i]):
    for aj,bj in enumerate(d[j]):
        for ak,bk in enumerate(d[k]):
            for al,bl in enumerate(d[l]):
                if i*ai+j*aj+k*ak+l*al<=W:
                    ans=max(ans,bi+bj+bk+bl)

print(ans)
