W, H, N = map(int, input().split())
r = [[1] * H for _ in range(W)]

for i in range(N):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        for i in range(x):
            for j in range(H):
                r[i][j] = 0
    if a == 2:
        for i in range(x,W):
            for j in range(H):
                r[i][j] = 0
    if a == 3:
        for i in range(W):
            for j in range(y):
                r[i][j] = 0
    if a == 4:
        for i in range(W):
            for j in range(y,H):
                r[i][j] = 0
print(sum(sum(R) for R in r))
