import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y, matrix, visited, isWhite):
    global black, white
    dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    visited[y][x] = True
    w = len(matrix[0])
    h = len(matrix)

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if nx < 0 or w <= nx or ny < 0 or h <= ny:
            continue

        if visited[ny][nx] is True:
            continue

        if (matrix[ny][nx] == "#" and isWhite is False) or (
            matrix[ny][nx] == "." and isWhite is True
        ):
            continue

        if matrix[ny][nx] == "#":
            black += 1
        else:
            white += 1

        isWhite = not isWhite
        dfs(nx, ny, matrix, visited, isWhite)
        isWhite = not isWhite

    return


h, w = map(int, input().split())
matrix = [""] * h
for i in range(h):
    matrix[i] = input()

ans = 0
visited = [[False] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if matrix[i][j] == "#" and visited[i][j] is False:
            black = 1
            white = 0
            dfs(j, i, matrix, visited, False)
            ans += black * white

print(ans)
