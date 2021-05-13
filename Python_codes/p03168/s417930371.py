n = int(input())
P = list(map(float, input().split()))

DP = [[0]*(n+1) for _ in range(n+1)]
DP[0][0] = 1

for i in range(n):
  for j in range(n+1):
    if j==0:
      DP[0][i+1] = DP[0][i] * (1-P[i])
    else:
      DP[j][i+1] = DP[j][i] * (1-P[i]) + DP[j-1][i] * P[i]

ans = 0
for k in range(n//2+1, n+1):
  ans += DP[k][n]

print(ans)