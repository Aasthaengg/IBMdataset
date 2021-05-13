def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)

def lcm(a,b):
  d = (a*b) / gcd(a,b)
  print d
while True:
  try:
   x = map(int,raw_input().split(" "))
   a,b = x[0],x[1]
   print gcd(a,b),(a*b)/gcd(a,b)

  except EOFError:
    break