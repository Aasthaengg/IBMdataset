from collections import deque

h, w = map(int, input().split())
AA = [list(input()) for _ in range(h)]
# AA[h][w]
infi = 10 ** 5
kouho = []
ans = [[infi] * (w) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if AA[i][j] == "#":
            kouho.append((i, j, 0))
            ans[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


que = deque(kouho)
while que:
    py, px, d = que.popleft()
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if nx < 0 or nx >= w:
            continue
        if ny < 0 or ny >= h:
            continue
        if ans[ny][nx] == infi:
            ans[ny][nx] = d + 1
            que.append((ny, nx, d + 1))


cnt = 0
for i in range(h):
    for j in range(w):
        cnt = max(cnt, ans[i][j])

print(cnt)
