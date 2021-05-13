a, b, k = map(int, input().split())
if k <= a:
  print('{} {}'.format(a-k, b))
else:
  k -= a
  print('{} {}'.format(0, max(b-k, 0)))