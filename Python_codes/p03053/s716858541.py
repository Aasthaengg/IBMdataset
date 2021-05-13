from collections import deque

H,W=map(int,input().split())
A=["*"*(W+2) for _ in range(H+2)]

for i in range(1,H+1):
    A[i]="*"+input()+"*"

inf=float("inf")
Dist=[[inf]*(W+2) for _ in range(H+2)]
Q=deque()

for x in range(1,H+1):
    for y in range(1,W+1):
        if A[x][y]=="#":
            Dist[x][y]=0
            Q.append((x,y))

E=[(-1,0),(1,0),(0,-1),(0,1)]
while Q:
    (x,y)=Q.popleft()
    for (a,b) in E:
        if A[x+a][y+b]=="." and Dist[x+a][y+b]==inf:
            Dist[x+a][y+b]=Dist[x][y]+1
            Q.append((x+a,y+b))

Ans=0
for x in range(1,H+1):
    for y in range(1,W+1):
        Ans=max(Ans,Dist[x][y])
print(Ans)