import sys
input = sys.stdin.readline

h, n = map(int, input().split())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i] ,b[i] = map(int, input().split())

inf = float("inf")
# dp[i][j]:i-1番目までの魔法で体力をj減らした時の消耗魔力の最大値
dp = [[inf]*(h+2) for i in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(h+1):
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        dp[i+1][min(j+a[i],h)] = min(dp[i+1][min(j+a[i],h)],dp[i+1][j]+b[i])

print(dp[n][h])




