def knapsack(n, w, info):
  dp = [[0]*(w + 1) for i in range(n + 1)]

  for i in range(n):
    for j in range(w + 1):
      weight, value = info[i]
      if j < weight:
        dp[i + 1][j] = dp[i][j]
      else:
        dp[i + 1][j] = max(dp[i][j], dp[i][j - weight] + value)
  return dp

N,T = map(int,input().split())
food = []
for _ in range(N):
  food.append(list(map(int,input().split())))
food.sort(key= lambda x: x[0])
dp = knapsack(N,T,food)

C = [0]*(N+1)
for i in range(N)[::-1]:
  C[i] = max(C[i+1], food[i][1])

ans = 0
for i in range(N+1):
  ans = max(dp[i][-2] + C[i], ans)

print(ans)
