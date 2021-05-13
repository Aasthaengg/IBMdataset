from itertools import combinations

n, k = map(int, input().split())

if k > (n - 1) * (n - 2) // 2:
  print(-1)
else:
  print(n * (n - 1) // 2 - k)
  for i in range(1, n):
    print(i, n)
  edge = combinations(range(1, n), 2)
  for _ in range((n - 1) * (n - 2) // 2 - k):
    u, v = next(edge)
    print(u, v)