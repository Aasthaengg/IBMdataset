n, m, k = map(int, input().split())
exists = False
for i in range(n + 1):
  for j in range(m + 1):
    if i * m + j * n - 2 * i * j == k:
      exists = True
      break
  if exists:
    break
print('Yes' if exists else 'No')