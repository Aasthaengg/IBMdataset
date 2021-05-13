from decimal import *
import math
a,b,c = map(int,input().split())
A = Decimal(a).sqrt()
B = Decimal(b).sqrt()
C = Decimal(c).sqrt()
if A + B < C:
    print("Yes")
else:
    print("No")