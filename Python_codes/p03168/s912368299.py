N = int(input())
p = list(map(lambda x: float(x), input().split()))

#dp[i][h] = i+1番目までで表h枚の確率
dp = [[0]*(N+1) for i in range(N)]
dp[0][0] = 1-p[0]
dp[0][1] = p[0]

for i in range(1, N):
  for h in range(N+1):
    dp[i][h] = dp[i-1][h]*(1-p[i]) + (0 if h==0 else dp[i-1][h-1]*p[i])
    
print(sum(dp[N-1][int((N+1)/2):]))