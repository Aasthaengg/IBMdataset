N, W = map(int, input().split())
w0 = 0
Items = []
for _ in range(N):
    w, v = map(int, input().split())
    if _ == 0:
        w0 = w
        w = 0
    else:
        w -= w0
    Items.append((w, v))
# i個目までを見たときに、重さはk, j個使用
DP = [[[0] * (N * 4) for _ in range(N * 4)] for __ in range(N+1)]

for i, (w, v) in enumerate(Items, 1):
    for j in range(1, N * 4):
        if i < j:
            break
        for k in range(N * 4):
            if k < w:
                DP[i][j][k] = DP[i-1][j][k]
            else:
                DP[i][j][k] = max(DP[i-1][j][k], DP[i-1][j-1][k-w] + v)

ans = 0
for j, value in enumerate(DP[N]):
    for k, v in enumerate(value):
        if j * w0 + k <= W:
            ans = max(ans, v)
print(ans)

