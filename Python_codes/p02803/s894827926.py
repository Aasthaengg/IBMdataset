from collections import deque
import numpy as np

H,W = map(int,input().split())
maze = [input() for _ in range(H)]

ans = 0
for x in range(H):
    for y in range(W):
        #壁からはスタートできない
        if maze[x][y] == "#":
            continue

        distance = [[-1]*W for _ in range(H)]
        distance[x][y] = 0
        #start位置
        stack = deque([[x,y]])

        while stack:
            h,w = stack.popleft()
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                new_h, new_w = h+i, w+j
                if new_h < 0 or new_w < 0 or new_h >= H or new_w >= W:
                    continue
                elif maze[new_h][new_w] != "#" and distance[new_h][new_w] == -1:
                    distance[new_h][new_w] = distance[h][w]+1
                    stack.append([new_h, new_w])

        ans = max(ans, np.max(distance))

print(ans)