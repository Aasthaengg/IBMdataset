# -*- coding: utf-8 -*-
from collections import deque
H, W = map(int, input().split())
map = [list(input()) for i in range(H)]
checked = list()
queue = deque()
for x in range(H):
    checked.append(list())
    for y in range(W):
        if map[x][y]=="#":
            checked[x].append(True)
            queue.append((x, y, 0))
        else:
            checked[x].append(False)
neighbors = [(1,0), (0,1), (-1,0), (0,-1)]
while queue:
    x, y, res = queue.popleft()
    for dx, dy in neighbors:
        nx, ny = x+dx, y+dy
        if 0<=nx<H and 0<=ny<W:
            if not checked[nx][ny]:
                queue.append((nx, ny, res+1))
                checked[nx][ny] = True
print(res)
