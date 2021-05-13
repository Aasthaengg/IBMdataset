from functools import reduce
from operator import mul
N = int(input())
A = [int(i) for i in input().split()]

prod = reduce(mul, A)
numerator = prod
denominator = sum([prod // a for a in A])
print(numerator / denominator)