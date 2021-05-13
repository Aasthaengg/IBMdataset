h, w = map(int, input().split())
s = [[i == "#" for i in input()] for _ in range(h)]
dp = [[10**9] * w for _ in range(h)]
dp[0][0] = int(s[0][0])
for i in range(h):
    for j in range(w):
        a = dp[i - 1][j] + (not s[i - 1][j] and s[i][j])
        b = dp[i][j - 1] + (not s[i][j -1] and s[i][j])
        dp[i][j] = min(a, b,dp[i][j])
print(dp[-1][-1])
