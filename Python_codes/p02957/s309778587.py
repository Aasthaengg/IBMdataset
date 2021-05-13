import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy

def main():
    a,b = map(int, input().split())
    num = b - a
    if num%2 == 0:
        print(b - (num//2))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()