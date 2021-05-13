from fractions import gcd
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
def gcd_list(numbers):
    return reduce(gcd, numbers)
print(gcd_list(a))