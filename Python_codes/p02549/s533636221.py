N, K = map(int, input().split())
MOD = 998244353
move = []

for _ in range(K):
  L, R = map(int, input().split())
  move.append((L, R))

dp = [0]*N
dp[0] = 1
accumdp = [0, 1]

for i in range(1, N):
  for l, r in move:
    dp[i] += accumdp[max(i-l+1, 0)] - accumdp[max(i-r, 0)]
  dp[i] %= MOD
  accumdp.append((accumdp[-1] + dp[i])%MOD)

print(dp[-1])