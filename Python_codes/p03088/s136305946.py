
N = int(input())
mod = 10 ** 9 + 7

A = 0
C = 1
G = 2
T = 3

dp = [ [[[0 for c3 in range(4)]  for c2 in range(4)]  for c1 in range(4)] for n in range(N+1)]

dp[0][3][3][3] = 1

for n in range(N):
  for c1 in range(4):
    for c2 in range(4):
      for c3 in range(4):
        for new in range(4):
          if c2 == A and c1 == G and new == C: continue
          if c2 == A and c1 == C and new == G: continue
          if c2 == G and c1 == A and new == C: continue
          if c3 == A and c1 == G and new == C: continue
          if c3 == A and c2 == G and new == C: continue

          dp[n+1][c2][c1][new] += dp[n][c3][c2][c1]      

ans = 0
for c1 in range(4):
  for c2 in range(4):
    for c3 in range(4):
      ans += dp[N][c1][c2][c3]

print(ans % mod)