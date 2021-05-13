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

import numpy


if __name__ == '__main__':
    an = int(input())
    a = [i for i in input().split()]
    ans = len(set(a))

    if ans == 4:
        print("Four")
    else:
        print("Three")


