a,b=[int(x) for x in input().split()]
import math
def lcm(x, y):
  return (x * y) // math.gcd(x, y)
print(lcm(a,b))