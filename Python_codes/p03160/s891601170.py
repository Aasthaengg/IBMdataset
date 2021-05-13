n = int(input())
h = list(map(int,input().split()))
dp = [1e+10 for i in range(n)]
dp[0] = 0
for i in range(0,n):
    for j in range(1,3):
        p = i + j
        if p < n:
            dp[p] = min(dp[p],dp[i] + abs(h[i] - h[p]))
print(dp[n-1])