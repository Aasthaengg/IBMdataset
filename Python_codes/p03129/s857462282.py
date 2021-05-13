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
    
    if a[0] % 2 ==1:
        a[0] +=1


    if a[0]//2 >=a[1] :
        print("YES")
    else:
        print("NO")
