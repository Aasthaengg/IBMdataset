N=int(input())
L=[]
if N==1:
    print(1)
    exit()
for i in range(N):
    x,y=map(int, input().split())
    L.append((x,y))

D={}
for i in range(N-1):
    t1=L[i]
    L2=L[i+1:]
    for t2 in L2:
        x1,y1=t1
        x2,y2=t2
        d1=(x2-x1,y2-y1)
        d2=(x1-x2,y1-y2)
        if d1 in D:
            D[(x2-x1,y2-y1)]+=1
        else:
            D[(x2-x1,y2-y1)]=1
        if d2 in D:
            D[(x1-x2,y1-y2)]+=1
        else:
            D[(x1-x2,y1-y2)]=1

print(max(N-max(D.values()),0))
