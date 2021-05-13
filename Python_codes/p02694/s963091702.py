from math import floor
from decimal import *
X = int(input())
Y = Decimal(100)
n = 0
while Y < X :
    n += 1
    Y = Y+floor(Y / 100)
print(n)
