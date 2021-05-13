
import math
import itertools
import statistics
#import numpy as np
import collections
#n = int(input())
w, a, b = list(map(int, input().split()))
#a = list(map(int, input().split()))
a_end = a+w
b_end = b+w

if a_end < b:
    print(b-a_end)
elif (a <= b and b <= a_end) or (b <= a and a <= b_end):
    print(0)
else:
    print(a-b_end)