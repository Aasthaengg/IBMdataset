import sys
input = sys.stdin.readline
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]
lis = list(map(int, input().split()))
dp[0][0] = lis[0]
dp[0][1] = lis[1]
dp[0][2] = lis[2]
for i in range(1,n):
  lis = list(map(int, input().split()))
  for j in range(3):
    for k in range(3):
      if j==k:
        continue
      dp[i][k] = max(dp[i-1][j]+lis[k], dp[i][k])

print(max(dp[-1]))