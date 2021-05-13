from fractions import gcd
# from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
import sys
from bisect import *
import itertools
import copy
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7

input = sys.stdin.readline
#最初にソートしてるのに何故かヒープ使ってハマった
def main():
    n, c = map(int, input().split())
    stk = [tuple(map(int, input().split())) for i in range(n)]
    stk = sorted(stk, key=lambda x: x[0])

    ans = 1
    l = []
    l = [(stk[0][1], stk[0][2])]
    for i in range(1, n):
        ll = []
        for j in range(len(l)):
            v = l[j]
            if stk[i][2] == v[1]:
                if stk[i][0] < v[0]:
                    ll.append(v)
            else:
                if stk[i][0] - 0.5 < v[0]:
                    ll.append(v)
        ll.append(stk[i][1:])
        l = ll
        ans = max(ans, len(l))
    print(ans)


if __name__ == '__main__':
    main()
