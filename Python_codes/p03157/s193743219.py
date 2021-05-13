from sys import setrecursionlimit


def dfs(i, j, c):
    visited[i][j] = 1
    current.append((i, j))
    for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W and not visited[ni][nj]):
            continue
        if S[ni][nj] == c:
            continue
        dfs(ni, nj, not c)


setrecursionlimit(2 * 10 ** 5)
H, W = map(int, input().split())
S = [[c == "#" for c in input()] for _ in range(H)]

ans = 0
visited = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] and not visited[i][j]:
            current = []
            dfs(i, j, True)
            b, w = 0, 0
            for k, l in current:
                if S[k][l]:
                    b += 1
                else:
                    w += 1
            ans += b * w
print(ans)
