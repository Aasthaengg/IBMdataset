import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt, gcd
from copy import deepcopy
from functools import reduce



def main():
    n = int(input())
    x_list = []
    for i in range(n):
        x = int(input())
        x_list.append(x)

    l = list(set(x_list))
    print(len(l))


if __name__ == "__main__":
    main()
