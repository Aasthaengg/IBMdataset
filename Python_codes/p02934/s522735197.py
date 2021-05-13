from fractions import Fraction
N = int(input())
a = list(map(int, input().split()))
total = 0
for i in a:
    total += Fraction(1, i)
print(float(Fraction(1, total)))
