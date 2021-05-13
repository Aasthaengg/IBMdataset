N, M = map(int, input().split())
edge = [tuple(map(int, input().split())) for i in range(M)]
cost = [-float("inf")] * N
cost[0] = 0

for n in range(N-1):
  for m in range(M):
    a, b, c = edge[m]
    cost[b-1] = max(cost[b-1], cost[a-1] + c)

r = cost[-1]
for m in range(M):
    a, b, c = edge[m]
    cost[b-1] = max(cost[b-1], cost[a-1] + c)

print(r if cost[-1] == r else "inf")