H, W = map(int, input().split())
S = [0]*(H+2)
S[0] = '#'*(W+2)
S[H+1] = '#'*(W+2)
for h in range(1,H+1):
  S[h] = '#' + input() + '#'
mod = 10**9+7
dp = [[0]*(W+1) for _ in range(H+1)]
dp[1][1] = 1
for h in range(1,H+1):
  for w in range(1,W+1):
    if h==1 and w==1:
      continue
    if S[h][w]=='#':
      continue
    dp[h][w] += dp[h][w-1]+dp[h-1][w]
    dp[h][w] %= mod
print(dp[-1][-1])