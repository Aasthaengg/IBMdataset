n,k = map(int,input().split())
h = list(map(int,input().split()))

dp = [10**10]*n
dp[0] = 0

for i in range(n-1):
    for j in range(i+1,min(i+k,n-1)+1):
        dp[j] = min(dp[j],dp[i]+abs(h[j]-h[i]))
        # print(dp)
print(dp[n-1])