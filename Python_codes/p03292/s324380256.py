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
    lis = list(map(int, input().split()))
    lis.sort(reverse=True)
    count = 0

    for i in range(len(lis)-1):
        count += abs(lis[i] - lis[i+1])
    print(count)

if __name__ == "__main__":
    main()