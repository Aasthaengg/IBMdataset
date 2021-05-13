
import math
import itertools
import statistics
#import collections
n, a, b = list(map(int, input().split()))
x = list(map(int, input().split()))

total = 0
for i in range(n-1):
    if (x[i+1]-x[i])*a < b:
        total += (x[i+1]-x[i])*a
    else:
        total += b

print(total)

