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
    c = a %500

    if c <= b:
        print("Yes")
    else:
        print("No")