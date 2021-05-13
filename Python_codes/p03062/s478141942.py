n = int(input())
A = list(map(int,input().split()))

dp = [[0]*2 for i in range(n)]

dp[0][0] = A[0]
dp[0][1] = -A[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][0]+A[i],dp[i-1][1]-A[i])
    dp[i][1] = max(dp[i-1][0]-A[i],dp[i-1][1]+A[i])

print(dp[n-1][0])