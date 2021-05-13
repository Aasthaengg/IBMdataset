p = 10**9+7
N,M = map(int,input().split())
A = {i:0 for i in range(N+1)}
for _ in range(M):
    A[int(input())] = 1
dp = [0 for _ in range(N+1)]
dp[N] = 1
for i in range(N-1,-1,-1):
    if A[i]==1:continue
    if A[i+1]==0:
        dp[i] = dp[i+1]
    if i+2<=N and A[i+2]==0:
        dp[i] = (dp[i]+dp[i+2])%p
print(dp[0])