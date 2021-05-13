n = int(input())
a = [[0] + list(map(int, input().split())) for _ in range(2)]
dp = [[0]*(n+1) for _ in range(2)]

for i in range(n):
    dp[0][i+1]=dp[0][i] + a[0][i+1]
    
for i in range(n):
    dp[1][i+1]=max(dp[1][i], dp[0][i+1])+a[1][1+i]

print(dp[1][n])        