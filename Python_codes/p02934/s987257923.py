from fractions import Fraction as frac
input()
a = list(map(int,input().split()))
sm = frac("1/" + str(a[0]))
for i in range(1,len(a)):
    sm += frac("1/" + str(a[i]))
print(sm.denominator / sm.numerator)