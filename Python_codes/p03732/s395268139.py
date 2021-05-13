n, w = map(int, input().split())
weights, values = zip(*[tuple(map(int, input().split()))for _ in range(n)])
min_w = min(weights)-1
weights = [weight-min_w for weight in weights]
W_MAX = 4*200
dp = [[0]*(W_MAX+1) for _ in range(n+1)]
for i in range(1, n+1):
    for k in reversed(range(1, n+1)):
        for j in range(1, W_MAX+1):
            if j-weights[i-1] < 0:
                continue
            dp[k][j] = max(dp[k][j], dp[k-1][j-weights[i-1]]+values[i-1])

ans = 0
for k in range(n+1):
    w_max = min(w-k*min_w, W_MAX)
    if w_max < 0:
        continue
    ans = max(ans, dp[k][w_max])
print(ans)