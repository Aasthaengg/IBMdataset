a, b, c, d = map(int, input().split())

if a*b != c*d:
  if a*b > c*d:
    print(a*b)
  else:
    print(c*d)
else:
  print(a*b)