from collections import deque


def bfs(que, maze, dis):
    max_x = len(maze[0])
    max_y = len(maze)

    while len(q) > 0:
        x, y, d = que.popleft()
        dxy = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 > nx or max_x <= nx or 0 > ny or max_y <= ny:
                continue
            if maze[ny][nx] == "#":
                continue
            if dis[ny][nx] != -1:
                continue

            dis[ny][nx] = d + 1
            que.append([nx, ny, dis[ny][nx]])

    return


h, w = map(int, input().split())
maze = [[] for _ in range(h)]
distance = [[-1] * w for _ in range(h)]

for i in range(h):
    maze[i] = input()

q = deque()

for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            q.append([j, i, 0])

bfs(q, maze, distance)

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, distance[i][j])

print(ans)
