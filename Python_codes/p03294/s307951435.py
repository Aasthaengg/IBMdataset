#103_C
import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
a = list(map(int, input().split()))

lcm = lcm_list(a)

ans = 0
for i in range(n):
    ans += (lcm-1) % a[i]
    
print(ans)