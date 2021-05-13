n,t = map(int,input().split())
ab = []
for i in range(n):
  a,b = map(int,input().split())
  ab.append([a,b])
dp = [0] * (t)
ab.sort()
m = 0
for i,j in ab:
  pdp,dp = dp,[0] * (t)
  for k in range(t):
    dp[k] = pdp[k]
  for k in range(t):
    if k+i >= t:
      m = max(m,pdp[k]+j)
    else:
      dp[k+i] = max(dp[k+i],pdp[k]+j)
if m == 0:
  print(max(dp))
else:
  print(m)