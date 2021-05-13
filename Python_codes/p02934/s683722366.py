import math
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
a=int(input())
b=list(map(int,input().split()))
n=lcm_list(b)
m=0
for i in b:
    m+=n//i
print(n/m)