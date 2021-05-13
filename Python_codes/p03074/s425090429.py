import bisect
# from collections import Counter, defaultdict, deque, namedtuple
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n, k = list(map(int,ipti().split()))
    s = input()

    lg = [0] * (n+3)

    s_first = s[0]
    s_last =s[-1]

    idx = 0

    if s_first == "0":
        lg[0] = 0
        idx = 1

    s_groupby = itertools.groupby(s)

    for _, group in s_groupby:
        lg[idx] = len(list(group))
        idx += 1

    if s_last == "0":
        idx += 1

    rn = 2*k + 1

    if rn >= idx:
        print(n)
        sys.exit()

    temp = sum(lg[0:rn])
    ans = temp

    for i in range(2, idx-rn+1, 2):
        temp -= (lg[i-2] + lg[i-1])
        temp += (lg[i-2+rn] + lg[i-1+rn])
        ans = max(ans, temp)

    print(ans)

if __name__ == '__main__':
    main()