# -*- coding: utf-8 -*-
H, W = map(int, input().split())
map = [list(input()) for i in range(H)]
cost_map =  [[None]*W for i in range(H)]
whites = 0
for i in range(H):
    for j in range(W):
        if map[i][j]==".":
            whites += 1
# 迷路を最短で抜ける
queue = list()
queue.append([0, 0])
cost_map[0][0] = 0
while queue:
    x,y = queue.pop(0)
    if x==H-1 and y==W-1:break
    current = cost_map[x][y]
    if 0<=x+1<H:
        if cost_map[x+1][y] is None and map[x+1][y]==".":
            queue.append([x+1, y])
            cost_map[x+1][y] = current + 1
    if 0<=x-1<H:
        if cost_map[x-1][y] is None and map[x-1][y]==".":
            queue.append([x-1, y])
            cost_map[x-1][y] = current + 1
    if 0<=y+1<W:
        if cost_map[x][y+1] is None and map[x][y+1]==".":
            queue.append([x, y+1])
            cost_map[x][y+1] = current + 1
    if 0<=y-1<W:
        if cost_map[x][y-1] is None and map[x][y-1]==".":
            queue.append([x, y-1])
            cost_map[x][y-1] = current + 1
# ゲーム開始時の白のマスの数から最短のマス目を引く
if cost_map[H-1][W-1] is None:
    print("-1")
else:
    print(whites - cost_map[H-1][W-1]-1)
