N = int(input())
height = list(map(int, input().split(" ")))
dp = [0]*N
 
for i in range(1,N):
  if i <= 2:
    dp[i] = abs(height[i]-height[0])
  else:
    dp[i] = min(dp[i-1] + abs(height[i]-height[i-1]), dp[i-2] + abs(height[i]-height[i-2]))

print(dp[N-1])