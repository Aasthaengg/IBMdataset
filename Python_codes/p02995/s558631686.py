a,b,c,d = map(int, input().split())

from math import gcd

def calc(a, b, n):
    return b//n - (a//n+bool(a%n))

print(b-a-calc(a,b,c)-calc(a,b,d)+calc(a,b,c*d//gcd(c,d)))