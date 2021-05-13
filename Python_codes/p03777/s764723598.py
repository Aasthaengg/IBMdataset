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

    if a[0] == "H" and a[1] =="H":
        print("H")
    elif a[0] == "D" and a[1] =="H":
        print("D")
    elif a[0] == "D" and a[1] =="D":
        print("H")
    else:
        print("D")