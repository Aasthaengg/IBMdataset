h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
grid = [[0] * w for _ in range(h)]
cnt = 0
color = []
for i in range(n):
    for j in range(a[i]):
        color.append(i + 1)
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            grid[i][j] = color[cnt]
            cnt += 1
    else:
        for j in range(w - 1, -1, -1):
            grid[i][j] = color[cnt]
            cnt += 1
for i in range(h):
    print(*grid[i])