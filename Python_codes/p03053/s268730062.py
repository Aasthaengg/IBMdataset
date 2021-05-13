h,w=map(int,input().split())
grid=[[-1]*w for _ in range(h)]
from collections import deque
que=deque()
for i in range(h):
    s=list(input())
    for j in range(w):
        if s[j]=='#':
            grid[i][j]=0
            que.append((i,j))
dirc=[(1,0),(-1,0),(0,1),(0,-1)]

while que:
    kuro=que.popleft()
    n=grid[kuro[0]][kuro[1]]
    for dx,dy in dirc:
        x=kuro[0]+dx
        y=kuro[1]+dy
        if 0<=x<h and 0<=y<w and grid[x][y]==-1:
            grid[x][y]=n+1
            que.append((x,y))

ans=0
for i in range(h):
    ans=max(ans,max(grid[i]))
print(ans)