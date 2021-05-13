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
    a = [str(i) for i in input().split()]

    if a[0][len(a[0])-1] ==a[1][0] and a[1][len(a[1])-1] ==a[2][0]:
        print("YES")
    else:
        print("NO")