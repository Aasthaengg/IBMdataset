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
    b, c = map(int, input().split())

    if b>c:
        print(b-c)
    else:
        print(0)