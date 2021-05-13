from collections import deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

cnt = [[10 ** 10] * w for _ in range(h)]
visited = [[0] * w for _ in range(h)]
queue = deque()
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            cnt[i][j] = 0
            queue.append([i, j])
            visited[i][j] = 1

def bfs(q, v, c):
    while q:
        y, x = q.popleft()
        for i, j in ([0, 1], [1, 0], [-1, 0], [0, -1]):
            ny = y + i
            nx = x + j
            if 0 <= nx < w and 0 <= ny < h and v[ny][nx] == 0:
                c[ny][nx] = c[y][x] + 1
                v[ny][nx] = 1
                q.append([ny, nx])

bfs(queue, visited, cnt)

ans = 0
for i in range(h):
    ans = max(ans, max(cnt[i]))
print(ans)