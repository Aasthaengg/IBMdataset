N = int(input()) 
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

dp = [[0] * N for i in range(2)]
dp[0][0] = A1[0]
dp[1][0] = A1[0] + A2[0]

for i in range(1, N):
  dp[0][i] = dp[0][i - 1] + A1[i]

for i in range(1, N):
  dp[1][i] = max(dp[1][i - 1], dp[0][i]) +  A2[i] 
  
#for i in range(2):
#  print(dp[i])

print(dp[-1][-1])