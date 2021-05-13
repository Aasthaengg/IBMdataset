from collections import deque
H, W = map(int, input().split())
a = []
for _ in range(H):
    a.append(input())
queue = deque([])
dist = [[-1 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if a[i][j] == "#":
            queue.append([i, j])
            dist[i][j] = 0
dh = [0, 0, 1, -1]
dw = [1, -1, 0, 0]
while queue:
    now = queue.popleft()
    h = now[0]
    w = now[1]
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh < 0 or nw < 0 or nh >= H or nw >= W:
            continue
        if dist[nh][nw] == -1:
            dist[nh][nw] = dist[h][w] + 1
            queue.append([nh, nw])
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, dist[i][j])
print(ans)