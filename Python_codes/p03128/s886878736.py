N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * N + [-1] * 9
for i in range(1, N+1):
    dp[i] = max(dp[i-int('0255456376'[a])] * 10 + a for a in A)

print(dp[N])