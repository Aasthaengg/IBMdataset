n = int(input())
probs = [float(i) for i in input().split()]
dp = [[0]*n for i in range(n)]
for i in range(n):
    if i==n//2:
        dp[n-1][i] = probs[n-1]
    elif i<n//2:
        dp[n-1][i] = 0 
    else:
        dp[n-1][i] = 1
for i in range(n-2, -1,-1):
    for j in range(i, -1,-1):
        dp[i][j] = probs[i] * dp[i+1][j+1] + (1-probs[i])*dp[i+1][j] 
print(dp[0][0])