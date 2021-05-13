MOD = 10**9 + 7
N = int(input())
C = [int(input()) for i in range(N)]
dp = [0] * (N+1)
dp_c = [0] * (2*10**5+1)
pred_ci = 0
dp[0] = 1
for i, ci in enumerate(C, 1):
    if pred_ci == ci:
        dp[i] += dp[i-1]
        continue
    dp[i] = (dp[i-1] + dp_c[ci]) % MOD
    dp_c[ci] = dp[i]
    pred_ci = ci

print(dp[N])