N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
a = set(a)
m = 10**9+7
dp = [0] * (N+1)
dp[0] = 1
for i in range(N):
    if i+1 not in a:
        dp[i+1] = (dp[i+1] + dp[i]) % m
    if i < N-1 and i+2 not in a:
        dp[i+2] = (dp[i+2] + dp[i]) % m
print(dp[N])