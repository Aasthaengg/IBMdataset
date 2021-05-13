import sys
import copy
import math
import bisect
import pprint
import bisect
from functools import reduce
from copy import deepcopy
from collections import deque
from decimal import *

import numpy as np

import math

if __name__ == '__main__':
    n, x = map(int, input().split())
    count =n
    list=[]
    for i in range(n):
        a = int(input())
        list.append(a)
    x -=sum(list)
    list.sort()
    count += x//list[0]
    print(count)
