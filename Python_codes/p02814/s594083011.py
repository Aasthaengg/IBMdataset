import fractions
import sys
from functools import reduce
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
  
N,M = (int(x) for x in input().split())
a = list(map(int,input().split()))
a = [a_i//2 for a_i in a]
lcm = lcm_list(a)
for a_i in a:
  if (lcm // a_i) %2 == 0:
    print(0)
    sys.exit()
  
print((M//lcm)//2 + ((M//lcm)%2==1))