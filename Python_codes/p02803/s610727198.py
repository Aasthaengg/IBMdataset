from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for i in range(H)]
XY = [(-1, 0), (1, 0), (0, 1), (0, -1)]

t_max = 0
for i in range(H):
    for j in range(W):
        step = [[0]*W for _ in range(H)]
        visited = [[False]*W for _ in range(H)]
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if maze[x][y] == "#":
                continue
            if visited[x][y]:
                continue
            for dx, dy in XY:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= H-1 and 0 <= ny <= W-1:
                    step[nx][ny] = step[x][y] + 1
                    queue.append((nx, ny))
                    t_max = max(t_max, step[nx][ny])
            visited[x][y] = True

print(t_max-1)



