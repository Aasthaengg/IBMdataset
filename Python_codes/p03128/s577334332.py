n,m = map(int,input().split())
a = set(map(int,input().split()))
dp = [0]+[-float('inf')]*n
f = [0,2,5,5,4,5,6,3,7,6]
for i in range(n+1):
  for j in a:
    F = f[j]
    if F <= i:
      dp[i] = max(dp[i-F]*10+j,dp[i])
print(dp[n])