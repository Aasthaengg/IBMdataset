from collections import defaultdict
import bisect
n,m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
mod = 10**9+7
p = max(n,m)
if n>m:
  t.extend((0,)*(n-m))
else:
  s.extend((0,)*(m-n))
dp = [[1 for i in range(p+1)] for j in range(p+1)]
for i in range(1,p+1):
  for j in range(1,p+1):
    x = s[i-1]
    y = t[j-1]
    if x == y:
      dp[i][j] = (dp[i-1][j]+dp[i][j-1])%mod
    else:
      dp[i][j] = (dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1])%mod
print(dp[-1][-1])