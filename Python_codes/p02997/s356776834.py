from itertools import combinations

n, k = map(int, input().split())

border = (n - 1) * (n - 2) // 2

if k > border:
  print(-1)
else:
  print(n - 1 + border - k)
  comb = list(combinations([i for i in range(1, n + 1)], 2))
  for i, j in comb[:n - 1 + border - k]:
    print(i, j)