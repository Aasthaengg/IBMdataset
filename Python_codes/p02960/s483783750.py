S = input()[::-1]
L = len(S)
MOD = 10**9+7
N = 13
# 0~13
dp = [ [0]*13 for i in range(L+1)]
dp[0][0] = 1
mul = 1

for i in range(L):
  if S[i] == "?":
    for prev in range(N):
      for j in range(10):
        dp[i+1][(j*mul+prev)%N] += dp[i][prev]
        dp[i+1][(j*mul+prev)%N] %= MOD
  else:
    j = int(S[i])
    for prev in range(N):
      dp[i+1][(j*mul+prev)%N] += dp[i][prev]
      dp[i+1][(j*mul+prev)%N] %= MOD
  
  mul *= 10
  mul %= N

print(dp[-1][5])