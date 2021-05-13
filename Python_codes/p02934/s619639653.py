N = int(input())
A = list(map(int, input().split()))
 
from fractions import Fraction
def inverse(f):
    return Fraction(f.denominator,f.numerator)
 
ans = 0
for i in A:
    ans = ans + inverse(i)
 
print(float(inverse(ans)))