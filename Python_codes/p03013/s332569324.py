MOD = 10**9 + 7

N, M = map(int,input().split())
A = set()
for _ in range(M):
    A.add(int(input()))

dp = [1] * (N+1)

if 1 in A:
    dp[1] = 0

for i in range(N-1):
    if i+2 in A:
        dp[i+2] = 0
    else:
        dp[i+2] = (dp[i] + dp[i+1]) % MOD
    
print(dp[N])