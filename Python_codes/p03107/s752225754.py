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
    s = input()
    c_zero = s.count("0")
    c_one = s.count("1")
    num = min(c_one,c_zero)
    print(num*2)
    

if __name__ == "__main__":
    main()