h, w = map(int, input().split())
fld = [list(map(int, input().split())) for _ in range(h)]

ans = []
for i in range(h):
    for j in range(w):
        if fld[i][j] % 2 == 0:
            continue

        if j < w-1:
            if fld[i][j+1] % 2 == 1:
                ans.append((i+1, j+1, i+1, j+2))
                fld[i][j] -= 1
                fld[i][j+1] += 1
                continue

        if i < h-1:
            if fld[i+1][j] % 2 == 1:
                ans.append((i+1, j+1, i+2, j+1))
                fld[i][j] -= 1
                fld[i+1][j] += 1
                continue

        if j < w-1:
            ans.append((i+1, j+1, i+1, j+2))
            fld[i][j] -= 1
            fld[i][j+1] += 1
            continue

        if i < h-1:
            ans.append((i+1, j+1, i+2, j+1))
            fld[i][j] -= 1
            fld[i+1][j] += 1
            continue


print(len(ans))
for row in ans:
    print(*row)
