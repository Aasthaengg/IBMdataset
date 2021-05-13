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
    a = int(input())
    b = int(input())
    c = int(input())
    big = max(a,b)
    count =0
    if c % big > 0:
        count = c//big +1
    else:
        count = c//big
    

    print(count)
