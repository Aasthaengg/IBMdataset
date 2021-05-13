import sys
import copy
import math
import bisect
import pprint
import bisect
from functools import reduce
from copy import deepcopy
from collections import deque

if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    
    if a[1] % a[0] ==0:
        print(a[0]+a[1])
    else:
        print(a[1]-a[0])
