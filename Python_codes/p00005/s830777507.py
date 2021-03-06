def gcd(x, y):
  if x < y:
    tmp = x
    x = y
    y = tmp
  while True:
    if y == 0:
      break
    x = x % y
    tmp = x
    x = y
    y = tmp

  return x

def lcm(x, y):
  return x * y / gcd(x, y)

while True:
  try:
    a, b = map(int, input().split())
    print(gcd(a, b), int(lcm(a, b)))
  except EOFError:
    break