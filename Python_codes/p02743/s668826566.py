from decimal import Decimal
a,b,c=map(Decimal,input().split())
heiho=Decimal(0.5)
A=a**heiho
B=b**heiho
C=c**heiho
if A+B<C:
    print("Yes")
else:
    print("No")