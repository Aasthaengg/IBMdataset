n,k= map(int, input().split())
xy=[list(map(int,input().split())) for i in range(n)]

def check(x1,y1,x2,y2):
    cnt=0
    for node in xy:
        x,y=node
        if x1<=x<=x2 and y1<=y<=y2:
            cnt+=1
    return cnt

xlis=[]
ylis=[]
for itm in xy:
    x,y=itm
    xlis.append(x)
    ylis.append(y)
xlis.sort()
ylis.sort()

ans=10**20
from itertools import *
for tmp1 in combinations(xlis,2):
    for tmp2 in combinations(ylis,2):
        x1,x2=tmp1
        y1,y2=tmp2
        ret = check(x1,y1,x2,y2)
        if ret==k:
            ans=min(ans,(x2-x1)*(y2-y1))

print(ans)