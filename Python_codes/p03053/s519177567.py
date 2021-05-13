# -*- coding: utf-8 -*-
# 18:01 -> 18:36 (give up. TLE)
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

H, W = map(int, input().split())

A = []
black_deque = deque()

for i in range(H):
    A.append(list(input()))
    black_deque.extend([(i,j) for j in range(W) if A[i][j] == '#'])

if len(black_deque) == H*W:
    print(0)
    exit(0)

for x,y in black_deque:
    A[x][y] = 0

while len(black_deque) != 0:
    x,y = black_deque.popleft()
    depth = A[x][y]
    for k in range(4):
        new_x = x+dx[k]
        new_y = y+dy[k]
        if 0 <= new_x < H and \
           0 <= new_y < W and \
           A[new_x][new_y] == '.':
            black_deque.append((new_x, new_y))
            A[new_x][new_y] = depth+1

print(depth)