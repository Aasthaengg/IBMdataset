N = int(input())
A  = [int(input()) for i in range(N)]

dp = [-(10**10)]*N
dp[0] = A[1]-A[0]
for i in range(1,N-1):
    dp[i] = max(A[i+1]-A[i]+dp[i-1], A[i+1]-A[i])

print(max(dp))

