#!/usr/bin/env python3
from collections import deque


H, W = [int(str) for str in input().strip().split()]
A = [list(input().strip()) for _ in range(H)]


def bfs(starts):
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    dists = [[-1] * W for _ in range(H)]
    max_dist = 0
    que = deque()
    for start in starts:
        dists[start[0]][start[1]] = 0
        que.append(start)
    while len(que):
        ch, cw = que.popleft()
        for dh, dw in moves:
            nh, nw = ch + dh, cw + dw
            if (    0 <= nh < H 
                and 0 <= nw < W 
                and dists[nh][nw] == -1):
                dists[nh][nw] = dists[ch][cw] + 1
                que.append((nh, nw))
                max_dist = max(max_dist, dists[nh][nw])
    return max_dist


def solve():
    starts = ((i, j) for i in range(H) for j in range(W) if A[i][j] == '#')
    print(bfs(starts))


solve()
