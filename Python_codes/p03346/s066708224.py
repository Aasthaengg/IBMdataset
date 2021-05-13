n = int(input())
p = [int(input()) for i in range(n)]

dp = [0 for i in range(n+1)]

for x in p:
    dp[x] = dp[x-1]+1

print(n-max(dp))