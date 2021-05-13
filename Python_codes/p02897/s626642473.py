import math
import itertools
n = int(input())
 
if(n %2 == 1):
    d = int((n-1)/2) + 1
else:
    d = int(n/2)
 
ans = d/n
 
print('{:.08f}'.format(ans))