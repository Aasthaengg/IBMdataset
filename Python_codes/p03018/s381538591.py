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
    s = input()
    s = s.replace("BC", "P")
    s = s.replace("B", "T")
    s = s.replace("C", "T")
    s = s.split("T")
    ans = 0
    for ss in s:
        p = 0
        for i in range(len(ss) - 1, -1 ,-1):
            if ss[i] == 'P':
                p += 1
            elif ss[i] == 'A':
                ans += p
    print(ans)





    


if __name__ == '__main__':
    main()
