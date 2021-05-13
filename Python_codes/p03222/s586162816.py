h,w,k = map(int,input().split())
mod = 10**9+7
am = [1,1,2,3,5,8,13,21]
DP = [[0 for i in range(w+1)] for j in range(h+1)]
DP[0][1] = 1
for i in range(1,h+1):
  for j in range(1,w+1):
    DP[i][j] = (DP[i-1][j]*am[j-1]*am[w-j])%mod
    if j > 1:
      DP[i][j] += (DP[i-1][j-1]*am[j-2]*am[w-j])%mod
    if j < w:
      DP[i][j] += (DP[i-1][j+1]*am[j-1]*am[w-j-1])%mod
print((DP[h][k])%mod)