import sys
input=sys.stdin.readline
from collections import deque
H,W=map(int,input().split())
maze=[]
visited=[[None]*W for _ in range(H)]
q=deque([])
for i in range(H):
    a=input().rstrip()
    maze.append(a)
    for j in range(W):
        if a[j]=="#":
            visited[i][j]=0
            q.append([i,j])
ans=0
while q:
    h,w=q.popleft()
    for nh,nw in ([h+1,w],[h-1,w],[h,w+1],[h,w-1]):
        if nh<0 or nh>H-1 or nw<0 or nw>W-1:
            continue
        if visited[nh][nw]!=None:
            continue
        visited[nh][nw]=visited[h][w]+1
        ans=max(ans,visited[nh][nw])
        q.append([nh,nw])
print(ans)