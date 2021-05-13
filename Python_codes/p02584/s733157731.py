x, k, d = map(int,input().split())
x = abs(x)

m = x // d
p = k - m if m <= k else 0

if p == 0:
  print(x - (k*d))
else:
  x -= m * d
  if p & 1:
    print(abs(x - d))
  else:
    print(x)