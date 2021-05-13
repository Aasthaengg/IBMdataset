from decimal import *
a,b,c = map(int,input().split())
a,b,c = Decimal(a),Decimal(b),Decimal(c)
if a**Decimal(0.5) + b**Decimal(0.5) < c**Decimal(0.5):
    print('Yes')
else:
    print('No')
