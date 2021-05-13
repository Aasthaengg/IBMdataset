n, t = map(int, input().split())
min_cost = float('inf')
for _i in range(n):
  cost, time = map(int, input().split())
  if time <= t and cost <= min_cost:
    min_cost = cost

if min_cost == float('inf'):
  print('TLE')
else:
  print(min_cost)