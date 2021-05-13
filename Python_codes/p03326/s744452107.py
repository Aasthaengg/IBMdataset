import sys
readline = sys.stdin.readline

# きれいさ、おいしさ、人気度、でそれぞれ正負のどちらを目指すかを決める
# たとえば、人気度だけ負を目指す場合
# i個目のケーキを食べることで「きれいさの正の値 + おいしさの正の値 + 人気度 * -1」が
# 大きくなるときだけ更新するDPを考える
# dp[i] = [値, (きれいさ,おいしさ,人気度)]

N,M = map(int,readline().split())
cakes = [None] * N
for i in range(N):
  cakes[i] = list(map(int,readline().split()))

INF = -(10 ** 15)
ans = INF
for i in range(2 ** 3):
  base = [-1,-1,-1]
  for j in range(3):
    if (i >> j) & 1:
      base[j] = 1
  dp = [None] * (M + 1)
  for j in range(M + 1):
    dp[j] = [INF,[INF,INF,INF]]
  dp[0] = [0,[0,0,0]]
  for j in range(N):
    x,y,z = cakes[j]
    for k in range(M-1,-1,-1):
      if dp[k][0] == INF:
        continue
      newx = dp[k][1][0] + x * base[0]
      newy = dp[k][1][1] + y * base[1]
      newz = dp[k][1][2] + z * base[2]
      if dp[k + 1][0] < newx + newy + newz:
        dp[k + 1][0] = newx + newy + newz
        dp[k + 1][1][0] = newx
        dp[k + 1][1][1] = newy
        dp[k + 1][1][2] = newz
  if ans < dp[M][0]:
    ans = dp[M][0]
    
print(ans)  
