import collections
import itertools

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

dis = [[-1] * w for _ in range(h)]
dis[0][0] = 0
que = collections.deque()
que.append((0, 0))


while que:
    py, px = que.popleft()
    for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ny = py + dy
        nx = px + dx
        if 0 <= ny < h and 0 <= nx < w and dis[ny][nx] == -1 and maze[ny][nx] == ".":
            dis[ny][nx] = dis[py][px] + 1
            que.append((ny, nx))

if dis[h - 1][w - 1] == -1:
    print(-1)
else:
    cnt = 0
    for i, j in itertools.product(range(h), range(w)):
        if maze[i][j] == "#":
            cnt += 1
    print(h * w - cnt - dis[h - 1][w - 1] - 1)