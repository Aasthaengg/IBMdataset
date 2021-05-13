H,W = list(map(int,input().split()))

M = []
for i in range(H):
    M.append(list(input()))

from collections import deque

out = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for sx in range(0,W):
    for sy in range(0,H):
        if M[sy][sx]=="#":
            continue
        d = [[10**4] * W for i in range(H)]
        que = deque([])
        que.append((sy, sx))
        d[sy][sx] = 0
        while que:
            p = que.popleft()
            for i in range(4):
                ny = p[0] + dy[i]
                nx = p[1] + dx[i]
                if (0<=nx<W)and(0<=ny<H)and(M[ny][nx]!="#")and(d[ny][nx]==10**4):
                    que.append((ny, nx))
                    d[ny][nx] = d[p[0]][p[1]] + 1
                    out = max(d[ny][nx],out)
print(out)