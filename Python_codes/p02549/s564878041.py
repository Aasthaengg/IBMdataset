import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
LR = [tuple(map(int,readline().split())) for i in range(K)]
DIV = 998244353
dp = [0] * (N + 1)
dp[1] = 1
sdp = [0] * (N + 1)
sdp[1] = 1

for i in range(2, N + 1):
  for j in range(K):
    l_ind = i - LR[j][1] - 1
    r_ind = i - LR[j][0]
    if r_ind < 0:
      continue
    dp[i] += sdp[r_ind]
    if l_ind >= 0:
      dp[i] -= sdp[l_ind]
    dp[i] %= DIV
  sdp[i] = sdp[i - 1] + dp[i]
  sdp[i] %= DIV
  
print(dp[N])