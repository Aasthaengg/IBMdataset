n = int(input())
a = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1000

kabu = [0 for _ in range(n)]

for i in range(1,n):
    kabu[i-1] = dp[i-1] // a[i-1] 
    oturi = dp[i-1] - kabu[i-1]*a[i-1]
    dp[i] = max(kabu[i-1]*a[i]+oturi, dp[i-1])

print(dp[-1])