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
    n = int(input())
    p_list = list(map(int, input().split()))
    count = 0
    for i in range(0,n-2):
        if ((p_list[i] < p_list[i+1] < p_list[i+2]) or (p_list[i+2] < p_list[i+1] < p_list[i])):
            count += 1
    print(count)

if __name__ == "__main__":
    main()