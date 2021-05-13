s = input()
dp = [[0 for i in range(13)] for j in range(len(s)+1)]

mod = 10**9+7
dp[0][0] = 1

for i in range(len(s)):
  for j in range(10): #j=今見ている桁の数字
    if s[i] != "?" and int(s[i]) != j:
      continue
    for k in range(13): #k=一桁前までのあまり
      dp[i+1][(j+10*k)%13] += dp[i][k]
      dp[i+1][(j+10*k)%13] %= mod
      
print(dp[-1][5])