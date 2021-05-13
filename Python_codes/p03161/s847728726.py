n,k = map(int,input().split())
h = list(map(int,input().split()))
dp = [10**10]*n
dp[0] = 0
if n-1 <= k:
    print(abs(h[-1]-h[0]))
else:
    for i in range(1,k+1):
        dp[i] = abs(h[i]-h[0])
    for i in range(k+1,n): 
        for j in range(1,k+1):
            dp[i] = min(dp[i], dp[i-j] + abs(h[i]-h[i-j]))
    print(dp[-1])