import math
import bisect
from queue import Queue
from collections import deque

n = int(input())
a = [int(i) for i in input().split()]

a.sort()

b = a[n-1]
c = bisect.bisect_left(a,b//2)
d = max(c-1,0)

if(abs(b/2 - a[c]) < abs(b/2 - a[d])):
    print(b,a[c])
else:
    print(b,a[d])