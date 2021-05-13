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
    count = 0
    for i in s:
        if i == "+":
            count += 1
        else:
            count -= 1

    print(count)


if __name__ == "__main__":
    main()