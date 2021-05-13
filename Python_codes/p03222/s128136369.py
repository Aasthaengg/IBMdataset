mod = 10**9+7
H, W, K = map(int, input().split())
if W == 1:
    print(1)
    exit()
dp = [[0] * W for _ in range(H+1)]
dp[0][K-1] = 1
factor = [0] * (W-1)
for i in range(W-1):
    for j in range(1 << i):
        for k in range(i-1):
            if (j >> k) & (j >> (k+1)):
                break
        else:
            factor[i] += 1
for i in range(1, H+1):
    for j in range(W):
        for k in [-1, 0, 1]:
            if 0 <= j+k < W:
                left = max(min(j, j+k)-1, 0)
                right = max(W-max(j, j+k)-2, 0)
                dp[i][j] += dp[i-1][j+k] * factor[left] * factor[right]
        dp[i][j] %= mod
print(dp[H][0])
