N = int(input())
dp = [[0]*10 for _ in range(10)]

for i in range(1, N+1):
  if i%10==0: continue
  strI = str(i)
  f,l = strI[-1], strI[0]
  dp[int(f)][int(l)] += 1

res = 0
for i in range(1,10):
  for j in range(1,10):
    res += dp[i][j] * dp[j][i]

print(res)