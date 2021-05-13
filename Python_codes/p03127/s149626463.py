from math import gcd
from functools import reduce

N = int(input())
A = [int(i) for i in input().split()]

def gcd_list(numbers):
    return reduce(gcd, numbers)

g = gcd_list(A)
print(g)