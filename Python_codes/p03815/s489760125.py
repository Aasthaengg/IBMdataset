
import math
import itertools
import statistics
#import collections
x = int(input())

s =  x//11

if 11*s == x:
    ans = s*2
elif 11*s < x:
    if 11*s+6 >= x:
        ans = s*2+1
    else:
        ans = s*2+2
else:
    ans = s*2-1

#print(11*s)
print(ans)