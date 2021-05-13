N,K = map(int,input().split())
h = list(map(int,input().split()))
inf = float("inf")
dp = [0]*N
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,N):
  cost = []
  for j in range(1,min(K,i)+1):
    cost.append(dp[i-j] + abs(h[i]-h[i-j]))
  dp[i] = min(cost)
print(dp[-1])