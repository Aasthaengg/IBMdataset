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
    count = (a[2] // a[0]) *a[1]
    print(count)
