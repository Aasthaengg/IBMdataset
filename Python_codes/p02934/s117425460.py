from fractions import Fraction
N = int(input())
A = [int(i) for i in input().split()]
print(float(1 / sum([Fraction(1, a) for a in A])))