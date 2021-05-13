from fractions import Fraction 
from math import floor
X,Y = input().split()
X = int(X)
Y = Fraction(Y)
print( floor(X*Y) )