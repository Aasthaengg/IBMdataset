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
    A, B = map(int, input().split())
    print(A + B if B % A == 0 else B - A)

main()
