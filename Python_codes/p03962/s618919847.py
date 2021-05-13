import sys
import math
from functools import reduce
import bisect


def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))


def input():
    return sys.stdin.readline().rstrip()


# input = sys.stdin.buffer.readline

def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return False


#############
# MAIN CODE #
#############

a, b, c = getNM()
print(len({a, b, c}))
