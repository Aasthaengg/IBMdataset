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
    a = int(input())
    b = int(input())
    c = int(input())
    ans = a -b
    ans = ans %c
    print(ans)