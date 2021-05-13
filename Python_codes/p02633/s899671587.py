def gcd(a, b):
  if a < b:
    a, b = b, a
  while a % b:
    a, b = b, a % b
  return b

x = int(input())
g = gcd(x, 360)
print(360 // g)