import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = [input() for i in range(H)]
visited = [[0] * W for i in range(H)]

def dfs(y, x):
    b, w = 0, 0
    if S[y][x] == '#': b += 1
    else: w += 1
    for dy, dx in ((0,1), (1,0), (0,-1), (-1,0)):
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
        if S[y][x] == S[ny][nx] or visited[ny][nx]: continue
        visited[ny][nx] = 1
        n, m = dfs(ny, nx)
        b += n
        w += m
    return (b, w)

ans = 0
for i in range(H):
    for j in range(W):
        if not visited[i][j]:
            visited[i][j] = 1
            b, w = dfs(i, j)
            ans += b * w
print(ans)
