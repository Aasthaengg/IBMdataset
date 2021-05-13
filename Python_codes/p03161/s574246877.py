INF = 10**9
N, K = map(int, input().split())
h = list(map(int, input().split()))
cost = [INF] * N
cost[0] = 0
for i in range(1, N):
  for j in range(1, min(i, K)+1):
    cost[i] = min(cost[i], cost[i-j] + abs(h[i] - h[i-j]))
print(cost[N-1])