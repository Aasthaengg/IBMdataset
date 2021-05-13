n, k = map(int, input().split())
pr = 0
for i in range(1, n+1):
  l = 0
  while i * 2**l < k:
    l += 1
  pr += 1 / (n * 2**l)
print(pr)