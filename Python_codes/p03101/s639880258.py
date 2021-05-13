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
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(a*b - (a*d + b*c-c*d) )

