from collections import deque

def bfs(a, b):
    global dist
    q = deque()
    q.append([a, b])
    bl, wh = 0, 0
    dist[a][b] = 0
    while q:
        p = q.popleft()
        x, y = p[0], p[1]
        if s[x][y] == "#":
            bl += 1
            for u in v:
                xx, yy = x + u[0], y + u[1]
                if s[xx][yy] == "." and dist[xx][yy] == -1:
                    dist[xx][yy] = dist[x][y] + 1
                    q.append([xx, yy])
        else:
            wh += 1
            for u in v:
                xx, yy = x + u[0], y + u[1]
                if s[xx][yy] == "#" and dist[xx][yy] == -1:
                    dist[xx][yy] = dist[x][y] + 1
                    q.append([xx, yy])
    return bl * wh

h, w = map(int, input().split())
s = [["$"] + list(input()) + ["$"] for _ in range(h)]
t = ["$"] * (w + 2)
s.insert(0, t)
s.append(t)
dist = [[-1] * (w + 2) for _ in range(h + 2)]
v = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if dist[i][j] == -1:
            ans += bfs(i, j)
print(ans)