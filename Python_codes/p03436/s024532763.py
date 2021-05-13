from collections import deque

H, W = map(int, input().split())
s_l = [input() for _ in range(H)]
dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
results = [[0 for _ in range(W)] for _ in range(H)]
results[0][0] = 1

queue = deque()
queue.append((0, 0))

while queue:
    y, x = queue.popleft()
    if H - 1 == y and W - 1 == x:
        break
    for dy, dx in dist:
        ny = y + dy
        nx = x + dx
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
        if s_l[ny][nx] != "#" and results[ny][nx] == 0:
            results[ny][nx] = results[y][x] + 1
            queue.append((ny, nx))

ans = 0
if results[H - 1][W - 1] == 0:
    ans = -1
else:
    ans = sum([s.count(".") for s in s_l]) - results[H - 1][W - 1]

print(ans)
