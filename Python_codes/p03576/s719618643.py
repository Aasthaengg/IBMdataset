# 全探索する

import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())

P = [None] * N
for i in range(N):
  P[i] = list(map(int,readline().split()))

ans = 10 ** 18 * 4 + 1
for ix in range(N-1):
  for jx in range(ix,N):
    # X軸が決まる
    left = P[ix][0]
    right = P[jx][0]
    if left > right:
      left,right = right,left
    for iy in range(N-1):
      for jy in range(iy,N):
        up = P[iy][1]
        down = P[jy][1]
        if up < down:
          up,down = down,up
        d = abs(up - down) * abs(right - left)
        if d > ans:
          continue
        cnt = 0
        for i in range(N):
          if left <= P[i][0] <= right and down <= P[i][1] <= up:
            cnt += 1
        if cnt >= K:
          ans = d
print(ans)