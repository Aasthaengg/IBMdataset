def gcd(a, b):
  if b == 0:
    return a
  return gcd(b,  a % b)

def lcm(a, b):
  return a * b / gcd(a, b)

while True:
  try:
    a, b = map(int, raw_input().split())
  except EOFError:
    break
  print "%d %d" % (gcd(a, b), lcm(a, b))