from collections import deque
import sys
H,W=map(int,input().split())
A=[]
for i in range(H):
    a=list(input())
    A.append(a)
#多点スタートな最短路問題
q=deque()
dist=[[-1 for _ in range(W)]for i in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j]=="#":
            dist[i][j]=0
            q.append([i,j])

dx=[1,0,-1,0]
dy=[0,1,0,-1]
while(len(q)):
    h,w=q.popleft()
    #print(h,w)
    #print(q)
    for i in range(4):
        y=h+dy[i]
        x=w+dx[i]
        if (y<0)or(y>=H)or(x<0)or(x>=W):
            continue
        if dist[y][x]==-1:
            dist[y][x]=dist[h][w]+1
            q.append([y,x])
ans=0
#print(dist)
for i in range(len(dist)):
    ans=max(ans,max(dist[i]))
print(ans)