from collections import deque
INF = -1
H, W = map(int,input().split())
d = [[INF for i in range(W)] for j in range(H)]
tx = [1, 0, -1, 0]
ty = [0, 1, 0, -1]

q = deque()
for i in range(H):
    line = list(input())
    for j in range(W):
        if line[j] == '#':
            d[i][j] = 0
            q.append([i, j, 0])

ans = 0

while len(q) > 0:
    p = q.popleft()
    ans = max(ans, p[2])
    for i in range(4):
        nx = p[0] + tx[i]
        ny = p[1] + ty[i]
        if 0 <= nx <= H-1 and 0 <= ny <= W-1 and d[nx][ny] == INF:
            d[nx][ny] = p[2] + 1
            q.append([nx, ny, p[2]+1])

print(ans)