from itertools import combinations

n, k = map(int, input().split())

if k > (n - 1) * (n - 2) // 2:
  print(-1)
else:
  print(n - 1 + (n - 1) * (n - 2) // 2 - k)
  for i in range(2, n + 1):
    print(1, i)
  comb = list(combinations([i for i in range(2, n + 1)], 2))
  for i, j in comb[:(n - 1) * (n - 2) // 2 - k]:
    print(i, j)