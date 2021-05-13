n, k = map(int, input().split())

if n < k:
  print(1)
elif n % k == 0:
  print(0)
else:
  print(1)