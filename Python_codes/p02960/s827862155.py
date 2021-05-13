import sys
readline = sys.stdin.readline

conv = {}
for i in range(13):
  conv[i] = (i * 10) % 13

S = readline().rstrip()
N = len(S)
DIV = 10 ** 9 + 7

dp = [[0] * 13 for i in range(N)]

x0 = S[0]
if x0 == "?":
  for i in range(10):
    dp[0][i] = 1
else:
  dp[0][int(x0)] = 1
  
for i in range(1, N):
  x = S[i]
  if x == "?":
    for j in range(13):
      for k in range(10):
        dp[i][(conv[j] + k) % 13] += dp[i - 1][j]
        dp[i][(conv[j] + k) % 13] %= DIV
  else:
    for j in range(13):
      dp[i][(conv[j] + int(x)) % 13] += dp[i - 1][j]
      dp[i][(conv[j] + int(x)) % 13] %= DIV

print(dp[-1][5])