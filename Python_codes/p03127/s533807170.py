import math
from functools import reduce

N = int(input())
A = list(map(int, input().split()))


def gcd(*numbers):
    return reduce(math.gcd, numbers)

answer = gcd(*A)
print(answer)