H, W = map(int, input().split())
# maze = [list(map(int, input().split())) for i in range(H)]
maze = []
s_init_cnt = 0
for i in range(H):
    gyo = list(input())
    s_init_cnt += gyo.count('.')
    maze.append(gyo)

#print(maze)
#print(s_init_cnt)

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
reached = [[-1] * W for i in range(H)]
reached[0][0] = 1
from collections import deque


def bfs():
    d = deque([[0, 0]])
    while len(d) > 0:
        px, py = d.popleft()
        for dx, dy in direction:
            tx = px + dx
            ty = py + dy
            if tx >= H or ty >= W or tx < 0 or ty < 0:
                continue
            if reached[tx][ty] != -1 or maze[tx][ty] == '#':
                continue
            else:
                reached[tx][ty] = reached[px][py] + 1
                d.append([tx, ty])
bfs()
ans = reached[H-1][W-1]
if ans == -1:
    print(ans)
else:
    ans = s_init_cnt - ans
    print(ans)
