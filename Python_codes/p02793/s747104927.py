n = int(input())
A =list(map(int, input().split()))
mod =10**9+7

import fractions
#import math
from functools import reduce
def lcm_base(x, y):
  return (x * y) // fractions.gcd(x, y)
  #return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
  return reduce(lcm_base, numbers, 1)

l = lcm_list(A)
ans = 0
for i in range(n):
    ans += l//A[i]
ans %= mod
print(ans)
