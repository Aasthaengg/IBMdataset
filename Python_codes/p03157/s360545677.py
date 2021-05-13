h, w = map(int, input().split())
grid = [[1 if i == "#" else 0 for i in input()] for _ in range(h)]
seen = [[0] * w for _ in range(h)]
DX = (0, 1, 0, -1)
DY = (1, 0, -1, 0)
ans = 0


def dfs(X, Y, cnt):
    todo = [(X, Y)]
    seen[X][Y] = cnt
    black = 0
    white = 1
    while todo:
        x, y = todo.pop()
        now = grid[x][y]
        for dx, dy in zip(DX, DY):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w:  # インデックスが範囲外ならだめ
                continue
            if seen[nx][ny] == cnt or now == grid[nx][ny]:  # 既に見ていたり、白-白、黒-黒ならばだめ
                continue
            if 1-now:  # 現在位置が白色の場合
                black += 1
            else:
                white += 1
            seen[nx][ny] = cnt
            todo.append((nx, ny))
    return black*white


cnt = 1
for i in range(h):
    for j in range(w):
        if grid[i][j] or seen[i][j]:
            continue
        ans += dfs(i, j, cnt)
        cnt += 1

print(ans)
