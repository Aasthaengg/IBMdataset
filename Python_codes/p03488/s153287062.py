S=input()
x,y=map(int, input().split())
N=len(S)
now=0
xs=[]
ys=[]
count=0
for i in range(N):
    if S[i]=="F":
        now+=1
    else:
        if count%2==0:
            xs.append(now)
        else:
            ys.append(now)
        count+=1
        now=0
    if S[i]=="F" and i==N-1:
        if count%2==0:
            xs.append(now)
        else:
            ys.append(now)
#print(xs,ys)
from collections import defaultdict
D=defaultdict(int)

xnow=xs.pop(0)
D[xnow]=1
for i in range(len(xs)):
    dx=xs[i]
    ds=D.keys()
    D=defaultdict(int)
    for v in ds:
        D[v+dx]=1
        D[v-dx]=1
D=dict(D)
#print(D)
xok=x in D


D=defaultdict(int)
D[0]=1
for i in range(len(ys)):
    dy=ys[i]
    ds=D.keys()
    D=defaultdict(int)
    for v in ds:
        D[v+dy]=1
        D[v-dy]=1
D=dict(D)
#print(D)
yok=y in D


if xok and yok:
    print("Yes")
else:
    print("No")