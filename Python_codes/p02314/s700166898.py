n,m = map(int,input().split())
L = list(map(int,input().split()))
dp = [float('inf')]*50001
for i in range(len(L)):
    dp[L[i]] = 1
for i in range(2,50001):
    for j in range(len(L)):
        if i-L[j] >= 1:
            dp[i] = min(dp[i-L[j]]+1,dp[i])
print(dp[n])
