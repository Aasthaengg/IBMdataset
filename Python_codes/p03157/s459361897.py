from collections import deque

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
visited = [[0]*w for _ in range(h)]
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

ans = 0
for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            bcnt, wcnt = 0, 0
            q = deque([(i, j)])
            while q:
                cx, cy = q.popleft()
                if visited[cx][cy]:
                    continue
                if grid[cx][cy] == "#":
                    bcnt += 1
                else:
                    wcnt += 1
                visited[cx][cy] = 1
                for (dx, dy) in moves:
                    if 0 <= cx + dx < h and 0 <= cy + dy < w and not visited[cx + dx][cy + dy] and grid[cx + dx][cy + dy] != grid[cx][cy]:
                        q.append((cx + dx, cy + dy))
            ans += bcnt * wcnt
print(ans)