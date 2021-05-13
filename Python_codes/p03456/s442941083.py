import sys
import math

A,B=input().split()
X=int(A+B)

print('Yes' if math.sqrt(X).is_integer() else 'No')