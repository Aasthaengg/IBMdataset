n = int(input())
A = list(map(int, input().split()))

import fractions
#import math
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)
    #return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
    #return reduce(math.gcd, numbers)

g = gcd_list(A)
print(g)
