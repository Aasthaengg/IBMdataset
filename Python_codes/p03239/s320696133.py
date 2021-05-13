N, T = map(int, input().split())
cost = 10000

for i in range(N):
  c, t = map(int, input().split())
  if t <= T:
    cost = min(cost, c)
    
if cost == 10000:
  print('TLE')
else:
  print(cost)