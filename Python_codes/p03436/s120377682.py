from collections import deque

H,W = map(int, input().split())

s_lst = [[i for i in input()]for j in range(H)]

dist = [[-1 for i in range(W)] for i in range(H)]
dist[0][0] = 1
d = deque()
d.append([0,0])

white_cnt = 0
for i in range(H):
    for j in range(W):
        if s_lst[i][j] == ".":
            white_cnt += 1

dy_dx = [[1,0],[0,1],[-1,0],[0,-1]]

while d:
    x,y = d.popleft()
    for dx, dy in dy_dx:
        nx = x + dx
        ny = y + dy

        if 0>nx or W<=nx or 0>ny or H<=ny:
            continue

        if dist[ny][nx] != -1 or s_lst[ny][nx] == "#":
            continue
        d.append([nx,ny])
        dist[ny][nx] = dist[y][x] +1

if dist[H-1][W-1] == -1:
    print(-1)
else:
    print(white_cnt-dist[H-1][W-1])