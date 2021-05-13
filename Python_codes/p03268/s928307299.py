n, k = map(int, input().split())

if k % 2 == 1:
  c1 = n // k
  print(c1 ** 3)
if k % 2 == 0:
  c1 = n // k
  c2 = 0
  for i in range(1, n+1):
    if i % k == k // 2:
      c2 += 1
  print(c1 ** 3 + c2 ** 3)
