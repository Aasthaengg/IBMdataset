h, w = map(int, input().split())
a = [input() for _ in range(h)]
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if a[i][j] == '.':
            if i < h - 1:
                dp[i+1][j] = dp[i][j]
            if j < w - 1:
                dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % 1000000007
print(dp[h-1][w-1])