import fractions
from functools import reduce
def gcd_list(l):
    return reduce(fractions.gcd, l)
n = int(input())
A = list(map(int, input().split()))
print(gcd_list(A))