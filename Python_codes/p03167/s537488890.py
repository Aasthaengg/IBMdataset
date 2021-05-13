import sys
buf = sys.stdin.buffer

import numpy as np
MOD = 10 ** 9 + 7

H,W = map(int,buf.readline().split())

grid = np.frombuffer(buf.read(),dtype='S1').reshape(H,-1)[:,:W]

#print(grid)

MOD = 10 ** 9 + 7
dp = np.zeros(W, dtype = np.int64)
dp[0] = 1

for row in grid:
  #print(row == b"#")
  wall = (row == b'#')
  # 上から落としてくる
  dp[wall] = 0
  # 左から右に
  np.cumsum(dp, out = dp)
  # 壁の補正
  sub = np.maximum.accumulate(dp * wall)
  dp -= sub
  dp %= MOD

answer = dp[-1]
print(answer)