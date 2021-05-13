r ,d, x = [int(i) for i in input().split()]
res = x
for _ in range(10):
  res = res * r - d
  print(res)