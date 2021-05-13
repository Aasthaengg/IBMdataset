import math
from decimal import *

n = int(input())
c = str(input())
w = c.count('W')
c = c[::-1]
ans= 0
for i in range(w):
    if(c[i]!= 'W'):
        ans+=1
print(ans)