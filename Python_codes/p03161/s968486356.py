n,k  = map(int,input().split())
a = list(map(int,input().split()))
INF = 10**15
dp = [INF for _ in range(n)]
dp[0] = 0
for i in range(n):
    for j in range(1,k+1):
        if i+j <= n-1 :
            dp[i+j] = min(dp[i]+ abs(a[i+j] - a[i]) , dp[i+j])
print(dp[-1])
