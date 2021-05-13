# pypy
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

R, C, K = map(int, readline().split())
rcv = list(map(int, read().split()))
rc2v = {}
for rr, cc, vv in zip(rcv[::3], rcv[1::3], rcv[2::3]):
    rc2v[(rr-1, cc-1)] = vv

dp = [[[0]*4 for c in range(C)] for r in range(2)]
dp[0][0][1] = rc2v[(0, 0)] if (0, 0) in rc2v else 0

for c in range(1, C):
  for k in range(1, 4):
    v = rc2v[(0, c)] if (0, c) in rc2v else 0
    dp[0][c][k] = max(dp[0][c-1][k], dp[0][c-1][k-1]+v)

for r in range(1, R):
  rr = r % 2
  dp[rr][0][0] = max(dp[rr-1][0])
  v = rc2v[(r, 0)] if (r, 0) in rc2v else 0
  dp[rr][0][1] = dp[rr][0][0] + v
  for c in range(1, C):
    v = rc2v[(r, c)] if (r, c) in rc2v else 0
    temp_max = max(dp[rr-1][c])
    dp[rr][c][1] = max(dp[rr][c-1][1], max(dp[rr][c-1][0], temp_max)+v)
    for k in range(2, 4):
      dp[rr][c][k] = max(dp[rr][c-1][k], dp[rr][c-1][k-1]+v)
    
if R % 2:
  print(max(dp[0][-1]))
else:
  print(max(dp[-1][-1]))