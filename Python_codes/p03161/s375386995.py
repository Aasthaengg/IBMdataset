n,k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
dp = [float('inf')]*n
dp[-1] = 0
dp[-2] = abs(h[-1]-h[-2])

for i in range(n-3,-1,-1):
  for j in range(i+1,min(i+k+1,n)):
    dp[i] = min(dp[i],dp[j]+abs(h[i]-h[j]))
                
print(dp[0])
