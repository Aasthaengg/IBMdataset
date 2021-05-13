from collections import *
n=int(input())
l=list(map(int,input().split()))
x,y=[],[]
c=0
for i in range(0,n,2):
    x.append(l[i])
for i in range(1,n,2):
    y.append(l[i])
xx=-1
if(len(set(x))==1):
    xx=x[0]
else:
    d=defaultdict(int)
    for i in x:
        d[i]+=1
    m=0
    xx=-1
    for i in d:
        if(d[i]>m):
            xx=i
            m=d[i]
    c+=sum(d.values())-m
if(len(set(y))>1 or (len(set(y))==1 and y[0]==xx)):
    d=defaultdict(int)
    for i in y:
        d[i]+=1
    m=0
    yy=-1
    for i in d:
        if(d[i]>m and i!=xx):
            yy=i
            m=d[i]
    c+=sum(d.values())-m
cc=0
yy=-1
if(len(set(y))==1):
    yy=y[0]
else:
    d=defaultdict(int)
    for i in y:
        d[i]+=1
    m=0
    yy=-1
    for i in d:
        if(d[i]>m):
            yy=i
            m=d[i]
    cc+=sum(d.values())-m
if(len(set(x))>1 or (len(set(x))==1 and x[0]==yy)):
    d=defaultdict(int)
    for i in x:
        d[i]+=1
    m=0
    xx=-1
    for i in d:
        if(d[i]>m and i!=yy):
            xx=i
            m=d[i]
    cc+=sum(d.values())-m
print(min(cc,c))
