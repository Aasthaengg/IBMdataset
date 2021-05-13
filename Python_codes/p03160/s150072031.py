n = int(input())
h = list(map(int, input().split()))
 
dp = []
for i in range(n):
	dp.append(int(0))
dp[0] = 0
dp[1] = abs(h[0]-h[1])
 
for j in range(2,n):
	dp[j] = min(dp[j-1] + abs(h[j-1] - h[j]),dp[j-2] + abs(h[j-2] - h[j]))
  
print(dp[n-1])