a, b, c, d = map(int, input().split())
e = abs(a-b)
f = abs(b-c)
g = abs(c-a)
if (e <= d and f <= d) or g <= d:
  print('Yes')
else:
  print('No')