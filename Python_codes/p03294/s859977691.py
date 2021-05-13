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
    a_list = list(map(int, input().split()))

    print(sum(a_list)-n)

if __name__ == "__main__":
    main()