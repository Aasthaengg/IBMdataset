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
    
    n,d = map(int, input().split())
    ans = n / (d*2 + 1)

    if ans.is_integer():
        print(int(ans))
    else:
        print(int(ans) + 1)


if __name__ == "__main__":
    main()