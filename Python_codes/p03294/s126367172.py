from fractions import gcd
from functools import reduce
def lcm_base(x,y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
    
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
    
N = int(input())
a = [int(i) for i in input().split(" ")]

x = lcm_list(a)-1
Sum = 0
for a_ in a:
    Sum += x%a_
print(Sum)