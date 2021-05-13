import copy
from collections import deque

h, w = map(int,input().split())

maze_o = [0]*h
for i in range(h):
    maze_o[i] = list(input())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
#すべての "." をスタート位置にする
ans = 0
for y in range(h):
    for x in range(w):
        if maze_o[y][x] == "#":
            continue
        maze = copy.deepcopy(maze_o)
        distance = deque([0])
        rireki = deque([])
        stack = deque([(y, x)])
        maze[y][x] = "#"
        while stack:
            yy, xx = stack.popleft()
            d = distance.popleft()
            rireki.append(d)
            for dxi,dyi in zip(dx, dy):
                if not (0<=dxi+xx<w and 0<=dyi+yy<h):
                    continue
                if maze[dyi+yy][dxi+xx] == "#":
                    continue
                distance.append(d+1)
                stack.append((dyi+yy,dxi+xx))
                maze[dyi+yy][dxi+xx] = "#"
        ans = max(ans, max(rireki))
print(ans)