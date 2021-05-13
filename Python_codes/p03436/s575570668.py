import sys
INF = 10**18
sys.setrecursionlimit(10**6)
from collections import deque

def li():
    return [int(x) for x in input().split()]


H, W = li()

maze = []
wall_cnt = 0
for i in range(H):
    row = input()
    wall_cnt += row.count("#")
    maze.append(list(row))

seen = [[INF] * W for _ in range(H)]

sx, sy = 0, 0
gx, gy = W - 1, H - 1

todo = deque()

todo.append((sx, sy))
seen[sy][sx] = 0

dist = INF
while len(todo) > 0:
    x, y = todo.popleft()
    if x == gx and y == gy:
        dist = seen[y][x]
        break
    children = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for child in children:
        cx, cy = child
        # validation and seen check
        if 0 <= cx < W and 0 <= cy < H and maze[cy][cx] == '.' and seen[cy][cx] == INF:
            seen[cy][cx] = seen[y][x] + 1
            todo.append((cx, cy))

ans = H * W - wall_cnt - (dist + 1)
print(ans if dist != INF else '-1')