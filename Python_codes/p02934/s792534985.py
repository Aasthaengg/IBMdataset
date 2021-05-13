from fractions import Fraction
n=int(input())
a=[int(i) for i in input().split()]
def frac(n):
  return Fraction(1,n)
b=map(frac,a)
c=Fraction(1,sum(b))
print(float(c))
