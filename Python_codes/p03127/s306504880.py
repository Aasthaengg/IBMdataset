import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)
  
N = int(input())
L = list(map(int,input().split()))

print(gcd_list(L))