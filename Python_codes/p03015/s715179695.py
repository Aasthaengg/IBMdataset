# import bisect
# from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    l = input()
    l_len = len(l)

    if l == "1":
        print(3)
        sys.exit()

    #n-1桁まで
    a1 = pow(3 ,l_len-1, MOD)

    #1桁目を1で固定

    a2 = 0
    count = 1

    for i in range(1, l_len-1):
        if l[i] == "1":
            temp1 = pow(2,count,MOD)
            temp2 = pow(3,(l_len-i)-1,MOD)
            a2 += temp1 * temp2
            a2 %= MOD
            count += 1

    if l_len > 1:
        temp1 = pow(2,count,MOD)
        a2 += temp1
        a2 = a2 % MOD
        if l[-1] == "1":
            temp1 *= 2
            temp1 %= MOD
            a2 += temp1
            a2 %= MOD

    ans = (a1+a2) % MOD

    print(ans)

if __name__ == '__main__':
    main()
