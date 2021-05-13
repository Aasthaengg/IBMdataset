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
    ans = a[0].upper()[0] +a[1].upper()[0]+a[2].upper()[0]
    print(ans)