n, m = map(int,input().split())
C = list(map(int,input().split()))

dp = [float('inf')]*10**5

dp[0] = 0

for i in range(n+1):
    for c in C:
        dp[i] = min(dp[i-c]+1, dp[i])
        
print(dp[n])
