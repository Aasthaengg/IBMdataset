import sys
sys.setrecursionlimit(10 ** 7)

def dfs(i, j):
    visited[i][j] = True
    res_b = 0
    res_w = 0
    if N[i][j]:
        res_b += 1
    else:
        res_w += 1
    for di, dj in d:
        if i + di < 0 or i + di >= H or j + dj < 0 or j + dj >= W:
            continue
        if N[i][j] == N[i+di][j+dj]:
            continue
        if visited[i+di][j+dj]:
            continue
        tmp_b, tmp_w = dfs(i + di, j + dj)
        res_b += tmp_b
        res_w += tmp_w
    return res_b, res_w

H, W = map(int, input().split())
N = [[False] * W for _ in range(H)]
for i in range(H):
    s = input()
    for j in range(W):
        N[i][j] = (s[j] == "#")

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * W for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if not N[i][j]:
            continue
        if visited[i][j]:
            continue
        b, w = dfs(i, j)
        ans += (b * w)

print(ans)