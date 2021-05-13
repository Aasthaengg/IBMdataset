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
    count =0

    if a[0] ==1:
        count+=300000
    if a[1] ==1:
        count+=300000
    if a[0] ==2:
        count+=200000
    if a[1] ==2:
        count+=200000
    if a[0] ==3:
        count+=100000
    if a[1] ==3:
        count+=100000
    if a[0] == a[1]==1 :
        count+=400000
    print(count)
