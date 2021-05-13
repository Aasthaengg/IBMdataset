from collections import deque

H, W = map(int, input().split())
s = [input() for _ in range(H)]

adj = [[] for _ in range(W*H)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0

for i in range(H):
    for j in range(W):
        if s[i][j] == '#': continue
        ans += 1
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < H and 0 <= x < W:
                if s[y][x] == '.':
                    adj[W*i + j].append(W*y + x)

queue = deque([0])
visit = [-1] * (H*W)
visit[0] = 1

while queue:
    now = queue.popleft()
    for u in adj[now]:
        if visit[u] < 0:
            queue.append(u)
            visit[u] = visit[now] + 1

print(ans - visit[H*W-1]) if visit[H*W-1] > 0 else print(-1)