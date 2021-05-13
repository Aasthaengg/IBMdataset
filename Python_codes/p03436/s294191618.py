#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

H, W = map(int, input().strip().split())
s = [input() for i in range(H)]

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]
reached = np.zeros((H, W))
que_x = [0]
que_y = [0]
can_reach = False

for x, y in zip(que_x, que_y):
    if x == H - 1 and y == W - 1:
        can_reach = True
        break
    for i in range(4):
        next_x = x + direction_x[i]
        next_y = y + direction_y[i]
        if not(0 <= next_x < H) or not(0 <= next_y < W):
            continue
        if s[next_x][next_y] == '#':
            continue
        if reached[next_x][next_y] > 0:
            reached[next_x][next_y] = min(reached[next_x][next_y], reached[x][y] + 1)
            continue
        reached[next_x][next_y] = reached[x][y] + 1
        que_x.append(next_x)
        que_y.append(next_y)

res = 0
if can_reach:
    for i in range(H):
        for j in range(W):
            if s[i][j] == '.':
                res += 1
    res = res - reached[H-1][W-1] - 1
else:
    res = -1
print(int(res))
