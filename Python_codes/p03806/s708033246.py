N, Ma, Mb = map(int, input().split())

items = []
mas = []
mbs = []
costs = []
for i in range(N):
  ma, mb, c = map(int, input().split())
  mas.append(ma)
  mbs.append(mb)
  costs.append(c)

max_cost = 5000
dp = [[[max_cost for k in range((N+1)*10)] for j in range((N+1)*10)] for i in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
  for j in range(N*10):
    for k in range(N*10):
      if dp[i][j][k] == max_cost:
        continue
      if dp[i+1][j][k] > dp[i][j][k]:
        dp[i+1][j][k] = dp[i][j][k]
      if dp[i+1][j+mas[i]][k+mbs[i]] > dp[i][j][k] + costs[i]:
        dp[i+1][j+mas[i]][k+mbs[i]] = dp[i][j][k] + costs[i]
        
min_cost = max_cost
for wa in range(1, N*10):
  for wb in range(1, N*10):
    if (wa * Mb != wb * Ma):
      continue;
    if min_cost > dp[N][wa][wb]:
      min_cost = dp[N][wa][wb]

  
if min_cost == max_cost:
  print("-1")
else:
  print(min_cost)
