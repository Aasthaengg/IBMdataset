import collections
import math
import copy

H,W=map(int,input().split())

A=[list(str(input())) for i in range(H)]
#1<=sy<=R
d=[[-1 for j in range(W)]for i in range(H)]
inf=10**6
ans=0
queue=collections.deque()
for i in range(H):
    for j in range(W):
        if A[i][j]=='#':
            queue.append([i,j])
            d[i][j]=0

moves=[[1,0],[-1,0],[0,1],[0,-1]]

nax=0
while len(queue)>0:
    now=queue.popleft()
    for i in range(4):
        ny=now[0]+moves[i][0]
        nx=now[1]+moves[i][1]
        if 0<=ny and ny<H and 0<=nx and nx<W and A[ny][nx]=='.' and d[ny][nx]==-1:
            d[ny][nx]=d[now[0]][now[1]]+1
            nax=max(nax,d[ny][nx])
            queue.append([ny,nx])


print(nax)
