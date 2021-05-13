H, W, K = map(int, input().split())
dp = [[0]*(W+2) for _ in range(H+1)]
dp[0][1] = 1
mod = 10**9+7
for i in range(H):
    for j in range(1, W+1):
        t_1 = 0
        t_2 = 0
        t_3 = 0
        for k in range(2**(W-1)):
            s = format(k, "b")
            p = 0
            if len(s) != W-1:
                s = "0"*(W-1-len(s)) + s
            for l in range(1, len(s)):
                if s[l-1] == "1" and s[l] == "1":
                    p = 1
                    break
            q = 0
            if p == 0:
                if 0 <= j - 2 < len(s):
                    if s[j-2] == "1":
                        t_1 += 1
                        q = 1
                if j-1 < len(s):
                    if s[j-1] == "1":
                        t_3 += 1
                        q = 1
                if q == 0:
                    t_2 += 1
        dp[i+1][j-1] += dp[i][j]*t_1
        dp[i+1][j] += dp[i][j]*t_2
        dp[i+1][j+1] += dp[i][j]*t_3
        dp[i+1][j-1] %= mod
        dp[i+1][j] %= mod
        dp[i+1][j+1] %= mod

print(dp[H][K])