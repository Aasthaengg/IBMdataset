from math import sqrt
from decimal import Decimal
a=list(map(int,input().split()))
if Decimal(a[0]).sqrt()+Decimal(a[1]).sqrt()<Decimal(a[2]).sqrt():
    print("Yes")
else:
    print("No")
