from fractions import gcd
from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
import sys
from bisect import *
import itertools
import copy
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for i in range(n)]
    
    d = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            aaa = xy[i][0] - xy[j][0]
            bbb = xy[i][1] - xy[j][1]
            d[(aaa,bbb)]+=1
            
    t = 0
    for v in d.values():
        t = max(v , t)
    print(n - t)

    






    


if __name__ == '__main__':
    main()
