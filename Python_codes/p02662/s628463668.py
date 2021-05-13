import sys
readline = sys.stdin.readline

N, S = map(int, readline().split())
A = list(int(x) for x in readline().split())
MOD = 998244353

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(S+1):
        # 1,2のケース。jが変わらない遷移が2通りある。
        dp[i+1][j] = (dp[i+1][j] + dp[i][j] * 2) % MOD
        # 3のケース。j+A[i] <= Sならば、j+A[i]に遷移する。
        if j + A[i] <= S:
            dp[i+1][j+A[i]] = (dp[i+1][j+A[i]] + dp[i][j]) % MOD
print(dp[N][S])