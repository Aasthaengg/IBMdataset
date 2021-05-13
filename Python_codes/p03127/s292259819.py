import fractions
from functools import reduce
n=int(input())
A=list(map(int,input().split()))
def gcd(*numbers):
    return reduce(fractions.gcd,numbers)
print(gcd(*A))
