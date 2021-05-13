h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

res = []
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j < w - 1:
                    a[i][j+1] += 1
                    res.append([i+1, j+1, i+1, j+2])
                elif i < h - 1:
                    a[i+1][j] += 1
                    res.append([i+1, j+1, i+2, j+1])
    else:
        for j in range(w-1, -1, -1):
            if a[i][j] % 2 == 1:
                if j > 0:
                    a[i][j-1] += 1
                    res.append([i+1, j+1, i+1, j])
                elif i < h - 1:
                    a[i+1][j] += 1
                    res.append([i+1, j+1, i+2, j+1])

print(len(res))
for y1, x1, y2, x2 in res:
    print(y1, x1, y2, x2)