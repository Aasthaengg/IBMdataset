from fractions import Fraction

n, *xx = map(Fraction, open(0).read().split())

a, b, *xx = sorted(xx)

ans = (a+b)/2

for x in xx:
    ans = (ans+x)/2

print(float(ans))