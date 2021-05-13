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
    a = [str(i) for i in input().split()]

    count = 0

    for  i in a[0]:
        if "2" == i:
            count +=1
    print(count)
