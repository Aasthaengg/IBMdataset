N,A,B = map(int, input().split())
X = list(map(int, input().split()))

total_cost = 0
for i in range(N - 1):
  walk_cost = A * (X[i+1] - X[i])
  if walk_cost < B:
    total_cost += walk_cost
  else:
    total_cost += B

print(total_cost)