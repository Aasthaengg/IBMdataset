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
    a,b,k = map(int, input().split())
    n = min(a,b)
    num = []
    for i in range(1,n+1,1):
        if (a%i == 0) and (b%i == 0):
            num.append(i)

    num.sort(reverse=True)
    
    print(num[k-1])

if __name__ == "__main__":
    main()