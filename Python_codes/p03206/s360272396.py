import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *
from fractions import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

def main():
    D = int(input())
    if D == 25:
        print('Christmas')
    elif D == 24:
        print('Christmas Eve')
    elif D == 23:
        print('Christmas Eve Eve')
    else:
        print('Christmas Eve Eve Eve')

main()
