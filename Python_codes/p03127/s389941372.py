import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

N = int(input())
nums = [int(i) for i in input().split()]

print(gcd_list(nums))