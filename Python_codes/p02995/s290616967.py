a, b, c, d = map(int, input().split())
s = b//c-(a-1)//c
t = b//d-(a-1)//d

#import fractions
import math
from functools import reduce
def lcm_base(x, y):
  #return (x * y) // fractions.gcd(x, y)
  return (x * y) // math.gcd(x, y)

l = lcm_base(c, d)

r = b//l-(a-1)//l

#print(s, t, r)

ans = b-a+1-(s+t-r)
print(ans)
