n = int(input())
A = list(map(int,input().split()))

import math
from functools import reduce

def lcm(a:int,b:int):
    return a // math.gcd(a, b) * b

def lcm_list(numbers):
    return reduce(lcm, numbers)

x = lcm_list(A)
ans = 0
for a in A:
    ans += (x-1)%a

print (ans)
