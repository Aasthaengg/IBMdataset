W, H, N = map(int, input().split())
grid = [[0 for i in range(W)] for j in range(H)]
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for j in range(H):
            for k in range(x):
                grid[j][k] = 1
    elif a == 2:
        for j in range(H):
            for k in range(x, W):
                grid[j][k] = 1
    elif a == 3:
        for j in range(W):
            for k in range(y):
                grid[k][j] = 1
    else:
        for j in range(W):
            for k in range(y, H):
                grid[k][j] = 1

ans = 0
for i in range(H):
    for j in range(W):
        ans += grid[i][j]
print(H * W - ans)