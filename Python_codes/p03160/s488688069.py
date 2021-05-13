n = int(input())
a = list(map(int,input().split()))
INF = 10**15
dp = [INF for _ in range(n)]
dp[0] = 0
for i in range(n):
    if i+1 <= n-1 :
        dp[i+1] = min(dp[i]+ abs(a[i+1] - a[i]) , dp[i+1])
    if i+2 <= n-1:
        dp[i+2] = min(dp[i]+ abs(a[i+2] - a[i]) , dp[i+2])
print(dp[-1])