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
    flag = False
    count = 0
    
    for i in range(len(s)):
        if s[i].isupper():
            count += 1

    if count > 2:
        print("WA")
        sys.exit()
    count = 0
    for i in range(len(s)):
        if (i == 0 and s[i] == "A"):
            flag = True
        
        if (2 <= i < len(s)-1):
            if (s[i] == "C"):
                count += 1


    if count != 1:
        flag = False

    if flag:
        print("AC")
    else:
        print("WA")
    

if __name__ == "__main__":
    main()