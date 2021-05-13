N,MA,MB = map(int, input().split())
A = []
for _ in range(N):
  a,b,c = map(int, input().split())
  A.append([a,b,c])
  
# dp[i][ca][cb]
# i番目までのitemでaがca gram, bがcb gram 変えるときの最小コスト
# i:1-indexed. so max(i) = N
# maxca,maxcb = N*10
# max_cost(inf) > N *100
# N <= 40

gram_max = 410
cost_inf = 10000
dp = [[[ cost_inf for _ in range(gram_max)] for _ in range(gram_max)] for _ in range(N+1)]

dp[0][0][0] = 0
for i in range(1,N+1):
  a,b,c = A[i-1]
  for ca in range(0,gram_max):
    for cb in range(0,gram_max):
      dp[i][ca][cb] = min(dp[i][ca][cb], dp[i-1][ca][cb]) # なにもしない
      if ca-a >= 0 and cb-b >= 0:
        dp[i][ca][cb] = min(dp[i][ca][cb], dp[i-1][ca-a][cb-b] + c) 
        
ans = 10000
for ca in range(1,gram_max):
  for cb in range(1,gram_max):
    # ca:cb = MA:MB
    if MA*cb == MB*ca:
      ans = min(ans, dp[N][ca][cb])
      
print(ans if ans < 5000 else -1)