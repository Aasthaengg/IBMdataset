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
    s =input()


    if "C" in s and "F" in s and "F" in  s[s.index("C"):] :
        print("Yes")
    else:
        print("No")

