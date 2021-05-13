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
    num = int(input())
    h = list(map(int, input().split()))
    ans = 0

    m=0
    for i in range(0,num):
        for j in range(m,num):
            if j == num-1:
                ans += h[j]
                flag = True
                break
            if h[j] > h[j+1]:
                ans += h[j] - h[j+1]
                m = j
        if flag:
            break
    print(ans)

if __name__ == "__main__":
    main()
