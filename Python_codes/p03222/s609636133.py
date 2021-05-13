import itertools

H, W, K = map(int, input().split())
mod = 10**9+7
patterns = []
for p in itertools.product([0, 1], repeat=W-1):
    valid = True
    for i in range(W-2):
        if p[i] == p[i+1] == 1:
            valid = False
            break
    if valid:
        patterns += [p]

dp = [[0]*(W+1) for _ in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        for pattern in patterns:
            if j > 0 and pattern[j-1] == 1:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= mod
            elif j < W-1 and pattern[j] == 1:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod
            else:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod
print(dp[H][K-1])