S = input()
INF = 10**9+7
dp = [0,0,0]
N = 1
for i in range(len(S)):
  if S[i]=='A':
    dp[0] += N
    dp[0] %= INF
  elif S[i]=='B':
    dp[1] += dp[0]
    dp[1] %= INF
  elif S[i]=='C':
    dp[2] += dp[1]
    dp[2] %= INF
  else:
    a = dp[0]
    b = dp[1]
    dp[0] = N + dp[0]*3
    dp[1] = a + dp[1]*3
    dp[2] = b + dp[2]*3
    dp[0] %= INF
    dp[1] %= INF
    dp[2] %= INF
    N = (3*N)%INF
print(dp[2]%INF)
