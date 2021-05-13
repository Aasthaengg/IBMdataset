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

    for i in range(1,100000002):
        if a[0] % a[1]==0:
            print(-1)
            break

        if i ==10**9+1:
            print(-1)
            break
        if a[0]*i %a[1] >0:
            print(a[0]*i)
            break
        if a[0]*i >10**18 +1:
            print(-1)
            break

