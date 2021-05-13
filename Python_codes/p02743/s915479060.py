from decimal import Decimal,getcontext
from math import sqrt
# getcontext().prec = 10000 # 標準は28,精度を調節
a,b,c=map(Decimal,input().split())
print("Yes" if a.sqrt()+b.sqrt()<c.sqrt() else "No") # sqrt(a)とかだとfloatになるよ