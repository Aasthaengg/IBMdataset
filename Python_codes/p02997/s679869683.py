from itertools import combinations
n, k = map(int, input().split())
nc2 = (n - 1) * (n - 2) // 2
if nc2 < k:
  print('-1')
  exit()
print(n - 1 + (nc2 - k))  # M
for i in range(2, n+1):
  print(f'1 {i}')
for i in range(nc2 - k):
  combs = list(combinations(range(2, n+1), 2))
  print(f'{combs[i][0]} {combs[i][1]}')
