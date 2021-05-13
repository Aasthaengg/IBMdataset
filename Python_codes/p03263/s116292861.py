H, W = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(H)]
ans = []
for i in range(H):
    for j in range(W):
        if field[i][j] % 2 == 0:
            continue
        found = False
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and field[ni][nj] % 2:
                field[i][j] -= 1
                field[ni][nj] += 1
                found = True
                ans.append((i + 1, j + 1, ni + 1, nj + 1))
                break
        if not found:
            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and field[ni][nj] % 2 == 0:
                    field[i][j] -= 1
                    field[ni][nj] += 1
                    ans.append((i + 1, j + 1, ni + 1, nj + 1))
                    break
print(len(ans))
[print(i, j, ni, nj) for i, j, ni, nj in ans]
