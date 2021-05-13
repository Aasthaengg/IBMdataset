n = int(input())
h = [int(x) for x in input().split()]
dp = [0]*n
dp[n-2] = abs(h[n-1]-h[n-2])

for i in range(n-3,-1,-1):
  dp[i] = min(dp[i+1]+abs(h[i]-h[i+1]),dp[i+2]+abs(h[i]-h[i+2]))
  
print(dp[0])