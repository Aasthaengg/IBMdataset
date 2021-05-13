N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
MOD = 10**9 + 7
 
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1 if 1 not in a else 0
 
a = set(list(range(2,N+1))) - set(a)
for i in a:
    dp[i] = (dp[i-1] + dp[i-2]) % MOD
print(dp[N] % MOD)