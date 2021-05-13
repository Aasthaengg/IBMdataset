import sys

sys.setrecursionlimit(10**6)
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
seen = [[False] * w for _ in range(h)]

numb = 0
numw = 0


def dfs(x, y):
    global numb, numw
    seen[x][y] = True
    if s[x][y] == '#':
        numb += 1
    else:
        numw += 1
    for di in range(4):
        nx = x + dx[di]
        ny = y + dy[di]
        if (nx < 0 or nx >= h or ny < 0 or ny >= w):
            continue
        if s[x][y] == s[nx][ny]:
            continue
        if seen[nx][ny]:
            continue
        dfs(nx, ny)


ans = 0
for x in range(h):
    for y in range(w):
        if seen[x][y]:
            continue
        if s[x][y] == '.':
            continue
        numb = 0
        numw = 0
        dfs(x, y)
        ans += numb * numw
print(ans)
