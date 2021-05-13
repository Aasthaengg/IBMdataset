N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
dp[0] = 1000
for i in range(N-1):
    dp[i+1] = max(dp[i],(dp[i]//A[i])*A[i+1]+dp[i]-(dp[i]//A[i])*A[i])
print(dp[-1])