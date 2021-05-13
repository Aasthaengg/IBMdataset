import math
a,b = map(str,input().split())
c = int(a+b)
d = math.ceil(math.sqrt(c))
#print(d)
if d**2 == c:
    print('Yes')
else:
    print('No')