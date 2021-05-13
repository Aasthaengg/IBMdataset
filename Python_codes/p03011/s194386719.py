p, q, r = map(int, input().split())
x = p + q
y = q + r
z = r + p

if x<=y and x<=z:
  print(x)
elif y<=x and y<=z:
  print(y)
else:
  print(z)
