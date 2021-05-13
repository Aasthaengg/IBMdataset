X, Y = map(int, input().split())

def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x%y)

g = Y / gcd(X, Y)

if g == 1:
  print("-1")
else:
  if g == 2:
    g = 3
  else:
    g = 2
  ans = X * g
  if ans <= 1e18:
    print(ans)
  else:
    print("-1")
