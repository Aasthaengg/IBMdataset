import sys
input=sys.stdin.readline
h,w,n = map(int, input().split())
l=[list(map(int,input().split())) for i in range(n)]

from collections import defaultdict
d = defaultdict(int)
for tmp in l:
    y=tmp[0]-1
    x=tmp[1]-1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 1<=x+i<w-1 and 1<=y+j <h-1:
                s = str(x+i) + "_" + str(y+j)
                d[s]+=1

import collections
lis = list(d.values())
c = collections.Counter(lis)

ans=[0]*10
for itm in c.items():
    ans[itm[0]]=itm[1]

ans[0]=(h-2)*(w-2)-sum(ans)

for a in ans:
    print(a)