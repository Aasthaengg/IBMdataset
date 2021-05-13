import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt
from copy import deepcopy

def main():
    n = int(input())
    
    if n < 4:
        print("No")
        sys.exit()
        
    if n%4 == 0 or n%7 == 0:
        print("Yes")
        sys.exit()

    while(n > 0):
        n -= 7
        if n%4 == 0:
            break

    if n >= 0:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()