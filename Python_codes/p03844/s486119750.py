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
    a,b, c = map(str ,input().split())
    ans = 0
    if b == "+":
        ans = int(a)+int(c)
    else:
        ans = int(a)-int(c)

    print(ans)

