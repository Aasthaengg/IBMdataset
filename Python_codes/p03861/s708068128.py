import math
from decimal import Decimal
(a,b,x)=map(Decimal, input().split(" "))
print(math.floor(b/x)-math.floor((a-1)/x))