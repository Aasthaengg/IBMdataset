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
    a1 =0
    a2=0
    a3=0
    a4=0
    for i in a:
        if i == 1:
            a1+=1
        if i == 9:
            a2+=1
        if i == 7:
            a3+=1
        if i == 4:
            a4+=1
    if a1 == a2==a3==a4 ==1:
        print("YES")
    else:
        print("NO")