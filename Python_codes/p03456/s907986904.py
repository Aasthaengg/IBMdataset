import math
a,b = map(int,input().split())
x = int(str(a)+str(b))
if math.sqrt(x) == int(math.sqrt(x)):
    print('Yes')
else:
    print('No')