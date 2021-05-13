y,m,d=map(int,input().split("/"))
from datetime import date
d1 = date(y, m, d)
d2 = date(2019, 4, 30)
print ("Heisei" if d1 <= d2 else "TBD")