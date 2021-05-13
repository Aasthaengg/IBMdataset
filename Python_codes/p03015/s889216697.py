L = str(input())

n = len(L)
MOD = 10**9+7
 
dp = [[0]*2 for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
  for k in range(2):
    nd = int(L[i])
    for d in range(2):
      ni = i+1
      nk = k
      if k == 0:
        if d > nd:
          continue
        elif d < nd:
          nk = 1
        else:
          pass
      if d == 1:
        dp[ni][nk] += (dp[i][k]*2)%MOD
      else:
        dp[ni][nk] += (dp[i][k])%MOD
        
#print(dp)
print(sum(dp[-1])%MOD)