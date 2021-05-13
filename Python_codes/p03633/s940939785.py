import math
from functools import reduce

def lcm2(x, y):
    return (x * y) // math.gcd(x, y) 

def lcm(nums):
    return reduce(lambda x, y: lcm2(x, y), nums)

N = int(input())
T = []

for _ in range(N):
    T.append(int(input()))

print(lcm(T))