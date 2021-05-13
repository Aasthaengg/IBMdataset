import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import decimal


if __name__ == "__main__":
    s = input()
    d = ""
    c = ""
    ans = 0
    for i in s:
        d += i
        if d != c:
            c = d
            d = ""
            ans+=1
    print(ans)