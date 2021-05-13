from decimal import Decimal
import math
a,b,n = map(str,input().split())

a = Decimal(a)
b = Decimal(b)
n = int(n)
ans = 0
kouho = [min(b-1,n)]
for x in kouho:
    tmp = math.floor((a*x)/b) - a*math.floor(x/b)
    ans = max(ans,tmp)
print(ans)