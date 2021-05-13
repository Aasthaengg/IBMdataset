from decimal import *
from math import *
l=list(map(int,input().split()))
x=Decimal(l[0])**(Decimal(0.5))
y=Decimal(l[1])**(Decimal(0.5))
z=Decimal(l[2])**(Decimal(0.5))
if(x+y<z):
    print("Yes")
else:
    print("No")