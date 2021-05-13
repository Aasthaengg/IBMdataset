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
    a,b, c = map(int, input().split())

    if abs(a-b) <abs(a-c):
        print("A")
    else:
        print("B")