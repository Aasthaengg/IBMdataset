a,b = input().split()
c = a+b
c = int(c)
import math
if(int(math.sqrt(c)) ** 2 == c):
    print('Yes')
else:
    print('No')