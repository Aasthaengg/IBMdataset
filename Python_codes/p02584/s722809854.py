x, k, d = map(int, input().split())
if x < 0:
  x *= -1
if x >= k * d:
  print(x - (k * d))
else:
  k -= x // d
  x = x % d
  if k % 2 == 0:
    if x < abs(x - (2 * d)):
      print(x)
    else:
      print(abs(x - 2 * d))
  else:
    if abs(x - d) < abs(x + d):
      print(abs(x - d))
    else:
      print(abs(x + d))