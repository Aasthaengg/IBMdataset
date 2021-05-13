N, S = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
dp = [0 for j in range(S + 1)]
dp[0] = 1
for i in range(N):
    for j in reversed(range(S + 1)):
        dp[j] = (2*dp[j])%mod if j < A[i] else (2*dp[j] + dp[j-A[i]])%mod
print(dp[S])