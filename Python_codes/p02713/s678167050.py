k = int(input()) + 1

import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

ans = 0

for a in range(1,k):
    for b in range(1,k):
        for c in range(1,k):
            ans += gcd(a,b,c)

print(ans)
