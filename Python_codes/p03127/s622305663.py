import math
from functools import reduce
 
def gcd(numbers):
    return reduce(math.gcd, numbers)
 
n=int(input())
A=tuple(map(int,input().split()))
print(gcd(A))