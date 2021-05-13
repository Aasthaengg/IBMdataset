import math

n=int(input())

XY=[]

for i in range(n):
    x,y=map(int,input().split())
    XY.append([x,y])

v=[]

for i in range(n):
    for j in range(n):
        if j!=i:
            v.append([XY[i][0]-XY[j][0],XY[i][1]-XY[j][1]])


c=0
for vx,vy in v:
    cv=0
    for i in range(n):
        for j in range(n):
            if j!=i and [XY[i][0]-XY[j][0],XY[i][1]-XY[j][1]]==[vx,vy]:
                cv+=1
    c=max(cv,c)

print(n-c)