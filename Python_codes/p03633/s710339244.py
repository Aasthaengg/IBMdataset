import sys,math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
  return reduce(lcm_base, numbers, 1)

n=int(input())
t=list(map(int,sys.stdin.read().split()))
print(lcm_list(t))

