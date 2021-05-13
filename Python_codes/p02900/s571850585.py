from math import floor, sqrt
from collections import defaultdict
from math import gcd
def factors(n):
    d = defaultdict(int)
    for i in range(2,floor(sqrt(n))+1):
        while n % i == 0:
            n //= i
            d[i] += 1
        if n == 1:
            break
    if n != 1:
        d[n] += 1
    return d

A,B = map(int,input().split())
N = gcd(A,B)
fac = factors(N)
print(len(fac)+1)