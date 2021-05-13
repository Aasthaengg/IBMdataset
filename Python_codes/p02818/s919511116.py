a, b, k = map(int, input().split())

if a >= k:
  print(a-k, end = ' ')
  print(b)
elif a + b <= k:
  print('0 0')
else:
  print(0, end = ' ')
  print(b - (k - a))