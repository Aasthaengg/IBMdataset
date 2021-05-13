N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

MOD = 10**9 + 7

safe = [True] * (N+1)
for i in range(len(A)):
    safe[A[i]] = False

dp = [0] * (N+1)
dp[0] = 1
if safe[1]:
    dp[1] = 1

for i in range(2, N+1):
    if(safe[i]):
        dp[i] = dp[i-1] + dp[(i-2)]
        dp[i] = dp[i] % MOD
    else:
        dp[i] = 0

print(dp[N])