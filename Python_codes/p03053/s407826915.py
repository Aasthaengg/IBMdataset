import sys
from collections import deque
input = sys.stdin.readline

H,W = map(int,input().split())
D = [list(input()) for i in range(H)]
ans = 0
dist = [[-1]*W for i in range(H)]
Q = deque()
dx = [1,0,-1,0]
dy = [0,-1,0,1]

for sy in range(H):
    for sx in range(W):
        if D[sy][sx] == "#":
            Q.append((sx,sy))
            dist[sy][sx] = 0
while Q:
    x,y = Q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<=W-1 and 0<=ny<=H-1 and dist[ny][nx] == -1 and D[ny][nx] == ".":
            Q.append((nx,ny))
            dist[ny][nx] = dist[y][x]+1

for y in range(H):
    for x in range(W):
        if D[y][x] == ".":
            ans = max(ans,dist[y][x])
print(ans)