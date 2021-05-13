import math
a,b=map(str,input().split())

dd=int(a+b)
sqq=int(math.sqrt(int(a+b)))
if dd==sqq**2:
    print('Yes')
else:
    print(('No'))

