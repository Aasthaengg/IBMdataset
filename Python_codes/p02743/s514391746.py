a, b ,c = map(int, input().split())
from decimal import Decimal
print("Yes") if Decimal(a).sqrt()+Decimal(b).sqrt()<Decimal(c).sqrt() else print("No")