import math
  
while True:
  try:
    a,b = list(map(int,input().split()))
    x = math.gcd(a,b)
    y = a * b // x
    print(x,y)
  except EOFError:
    break
