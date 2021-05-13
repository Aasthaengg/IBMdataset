#DP[i][j][k] = (i番目まで、j個選ぶ、有効重さの和kのときの最大得点)

N, W = map(int, input().split())
INF = 10**13
DP = [[[-INF for _ in range(3*N+1)] for _ in range(N+1)] for _ in range(N+1)]
w0, v = map(int, input().split())
DP[1][0][0] = 0
DP[1][1][0] = v

for i in range(2,N+1):
  w, v = map(int, input().split())
  w -= w0
  for j in range(N+1):
    for k in range(3*N+1):
      if k-w >= 0:
        DP[i][j][k] = max(DP[i-1][j-1][k-w] + v, DP[i-1][j][k])
      else:
        DP[i][j][k] = DP[i-1][j][k]

#print(w0)
#print(DP)
#print([max(DP[N][j]) + w0*j for j in range(N+1)])
#print(max([max(DP[N][j]) + w0*j for j in range(N+1)]))
ans = max([max([DP[N][j][k] for k in range(min(3*N,W-w0*j)+1)]) if W-w0*j >= 0 else -INF for j in range(N+1)])
print(ans)