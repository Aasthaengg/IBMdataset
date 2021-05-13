n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for i in range(m)]

for a, b in ab:
  cost, idx = 10**18, 0
  for i, (c, d) in enumerate(cd):
    if cost > abs(a - c) + abs(b - d):
      cost = abs(a - c) + abs(b - d)
      idx = i + 1
  print(idx)
