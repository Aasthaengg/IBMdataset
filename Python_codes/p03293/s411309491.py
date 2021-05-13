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
    ss = s + s 
    t = input()
    flag = False
    

    for i in range(len(s)):

        count = 0
        for j in range(len(s)):
            if t[j] == ss[i + j]:
                count += 1
        if count == len(s):
            flag = True

    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()