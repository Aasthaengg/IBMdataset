N,M = map(int,input().split())
A = [int(input()) for _ in range(M)]

isbroken = [1 for _ in range(N+1)]
for i in range(M):
  isbroken[A[i]] = 0


dp = [0 for _ in range(N+1)]
dp[0] = 1
mod = 10**9 + 7

dp[1] = dp[0] * isbroken[0]
  
for j in range(1,N):
  dp[j+1] = (dp[j] * isbroken[j] + dp[j-1] * isbroken[j-1]) % mod
    
print(dp[N])