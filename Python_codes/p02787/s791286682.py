H, N = map(int,input().split())
M = []
for k in range(N):
    M.append(list(map(int,input().split())))
dp = [10**9]*(10**5)
dp[0] = 0
for A, B in M:
    for k in range(A+1):
        dp[k] = min(dp[k],B)
    for k in range(A+1,H+1):
        dp[k] = min(dp[k],dp[k-A]+B)
print(dp[H])
