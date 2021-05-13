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
    s = input()
    t = input()

    min_num = 10**5
    max_num = 0
    count = 0
    for i in range(len(s) - len(t)+1):
        for j in range(len(t)):
            if s[i+j] == t[j]:
                count += 1
        if max_num <= count:
            max_num = count
        count = 0

    print(len(t) - max_num)

if __name__ == "__main__":
    main()