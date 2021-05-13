h, w = map(int, input().split())
a = [[] for _ in range(h)]

for i in range(h):
    a[i] = list(map(int, input().split()))

ans = []

for i in range(h):
    if i != h - 1:
        for j in range(w):
            if a[i][j] % 2 != 0:
                a[i + 1][j] += 1
                a[i][j] -= 1
                ans.append([i + 1, j + 1, i + 2, j + 1])
    else:
        for j in range(w - 1):
            if a[i][j] % 2 != 0:
                a[i][j + 1] += 1
                a[i][j] -= 1
                ans.append([i + 1, j + 1, i + 1, j + 2])


print(len(ans))

for y1, x1, y2, x2 in ans:
    print("%d %d %d %d" % (y1, x1, y2, x2))
