n = int(input())
pi = [int(input()) for i in range(n)]

dp = [0]*(n+1)

for i in range(n):
    dp[pi[i]] = dp[pi[i]-1] + 1
    
print(n-max(dp))