from collections import deque

def bfs():
    global ans
    while q:
        p = q.popleft()
        for u in v:
            x, y = p[0] + u[0], p[1] + u[1]
            if 0 <= x < h and 0 <= y < w:
                if s[x][y] == -1:
                    s[x][y] = s[p[0]][p[1]] + 1
                    q.append([x, y])
                    ans = max(ans, s[x][y])
    return

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
s = [[-1] * w for _ in range(h)]
v = [[1, 0], [-1, 0], [0, 1], [0, -1]]
q = deque()
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            s[i][j] = 0
            q.append([i, j])
bfs()
print(ans)