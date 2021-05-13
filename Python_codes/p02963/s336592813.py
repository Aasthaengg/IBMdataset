from math import sqrt, ceil
S = int(input())

"""
|x1y2 - x2y1| = S

"""

x1 = ceil(sqrt(S))
x2 = x1*x1 - S
print(0,0,x1,1,x2,x1)