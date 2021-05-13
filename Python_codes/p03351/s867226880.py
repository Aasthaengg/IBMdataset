import sys
import copy
import math
import bisect
import pprint
import bisect
from functools import reduce
from copy import deepcopy
from collections import deque

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

if __name__ == '__main__':
    a = [int(i) for i in input().split()]

    if abs(a[0]-a[2]) <=a[3] or (abs(a[0] -a[1]) <=a[3] and abs(a[1]-a[2]) <=a[3]):
        print("Yes")
    else:
        print("No")