a, b = map(int, input().split())
import fractions
#import math
from functools import reduce
def lcm_base(x, y):
  return (x * y) // fractions.gcd(x, y)
  #return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
  return reduce(lcm_base, numbers, 1)

print(lcm_base(a, b))
