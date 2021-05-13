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
    N = int(input())
    if N == 1:
        print('Hello World')
    else:
        print(int(input()) + int(input()))


main()
