from collections import *

H, W = list(map(int, input().split()))
S = [input() for i in range(H)]

ans = 0
INF = float('inf')

for i in range(H):
    for j in range(W):
        if S[i][j] == '#': continue

        dist = [[INF for i in range(W)] for j in range(H)]
        visited = [[False for i in range(W)] for j in range(H)]

        q = deque()
        q.append((i, j, 0))
        
        while q:
            i, j, c = q.popleft()

            if visited[i][j]: continue
            visited[i][j] = True
            dist[i][j] = c
            ans = max(ans, c)
            for a, b in [(1,0), (-1,0), (0,1), (0,-1)]:
                x = i+a
                y = j+b

                if 0 <= x < H and 0 <= y < W and S[x][y] == '.' and not visited[x][y]:
                    q.append((x, y, c+1))

print(ans)
