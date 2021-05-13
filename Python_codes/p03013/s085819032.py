MOD = 10**9+7

n, m = map(int,input().split())

A = [0]*(n+1)
for i in range(m):
    a = int(input())
    A[a] = 1

dp = [0]*(n+1)
dp[0] = 1
if not A[1]:
    dp[1] = 1

for i in range(2,n+1):
    if A[i]:
        continue
    dp[i] = (dp[i-1]+dp[i-2])%MOD

print(dp[n])