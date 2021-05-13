import fractions
from functools import reduce
 
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)
 
def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
 
 
N = int(input())
A = list(map(int,input().split()))
ans = gcd_list(A)
print(ans)