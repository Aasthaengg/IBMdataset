n = int(input())

dp = [1]*(n)
dp[0] = 0

for i in range(2, n):
  for j in range(i, n, i):
    dp[j] += 1
    
print(sum(dp))