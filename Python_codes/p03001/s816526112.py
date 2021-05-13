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
    w,h,x,y = map(int, input().split())
    print(w*h/2, int(w/2 == x and h/2 == y))
    

if __name__ == "__main__":
    main()