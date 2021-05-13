from collections import deque

H,W=map(int,input().split())
grid=[input() for i in range(H)]
dist=[[-1]*W for _ in range(H)]

M=deque()
for i in range(H):
    for j in range(W):
        if grid[i][j]=="#":
            M.append((i,j))
            dist[i][j]=0

def bfs(M,dist):
    d=0
    while M:
        x,y=M.popleft()
        d=dist[x][y]
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            new_h=x+dy
            new_w=y+dx
            if new_h < 0 or H <= new_h or new_w <0 or W <= new_w:
                continue
            if dist[new_h][new_w] == -1:
                dist[new_h][new_w]=d+1
                M.append((new_h,new_w))
    return d

d=bfs(M,dist)
print(d)

