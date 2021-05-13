import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush
from math import ceil, floor, sqrt, gcd
from copy import deepcopy

def main():
    a,b,c = map(int, input().split())
    if b//a >= c:
        print(c)
    else:
        print(b//a)
    

if __name__ == "__main__":
    main()