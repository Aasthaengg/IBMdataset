n,m = map(int, input().split())
A = list(map(int, input().split()))

C = [0,2,5,5,4,5,6,3,7,6]
dp = [-1]*(n+1)
dp[0] = 0

for n_i in range(n):
  for a_i in A:
    if n_i+C[a_i]<=n:
      dp[n_i+C[a_i]] = max(dp[n_i+C[a_i]], dp[n_i]*10+a_i)
      
print(dp.pop())