import math
from decimal import Decimal
a,b,x=map(int,input().split())
print(math.floor(Decimal(b)/Decimal(x))-math.ceil(Decimal(a)/Decimal(x))+1)