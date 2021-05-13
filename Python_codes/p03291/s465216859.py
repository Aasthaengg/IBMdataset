mod = 10**9+7
S = input()
l = len(S)
dp = [0,0,1]
ans = 0
for i in range(l):
    if S[i] == 'A':
        dp[0] += dp[2]
        dp[0] %= mod
    if S[i] == 'B':
        dp[1] += dp[0]
        dp[1] %= mod
    if S[i] == 'C':
        ans += dp[1]
        ans %= mod
    if S[i] == '?':
        dp1 = dp[:]
        dp2 = dp[:]
        dp3 = dp[:]
        dp1[0] += dp1[2]
        dp2[1] += dp2[0]
        ans *= 3
        ans += dp3[1]
        ans %= mod
        dp[0] = (dp1[0]+dp2[0]+dp3[0]) % mod
        dp[1] = (dp1[1]+dp2[1]+dp3[1]) % mod
        dp[2]*= 3
        dp[2] %= mod
print(ans)