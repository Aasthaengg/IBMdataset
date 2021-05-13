a, b, c, K = (int(x) for x in input().split())
if abs(a - b) > 10 ** 18:
  print('Unfair')
else:
  if K%2 == 0:
    print(a - b)
  else:
    print(b - a)