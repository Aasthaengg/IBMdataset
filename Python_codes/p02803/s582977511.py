from collections import deque
h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
dxdy = [(-1,0), (0,-1), (0,1), (1,0)]
INF = 10**5
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            continue
        q = deque([(i, j)])
        dist = [[INF]*w for _ in range(h)]
        dist[i][j] = 0
        while q:
            y, x = q.popleft()
            for dx, dy in dxdy:
                if not (0<=x+dx<w and 0<=y+dy<h):
                    continue
                if s[y+dy][x+dx]=='#' or dist[y+dy][x+dx]<INF:
                    continue
                dist[y+dy][x+dx] = dist[y][x] + 1
                q.append((y+dy, x+dx))
        for row in dist:
            for ele in row:
                if ele==INF:
                    continue
                ans = max(ans, ele)
print(ans)