from fractions import gcd
# from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
from bisect import *
import itertools
import fractions
# import sys
# sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
# input = sys.stdin.readline





def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    r = [a[0] % k]
    for i in range(1,n):
        r.append((r[i - 1] + a[i]) %k)
    
    d = defaultdict(int)
    r = [0] + r
    d[0] = 1
    ans = 0
    for i in range(n):
        if i >= k - 1:
            d[r[i - k  + 1]]-=1
        ans+=d[r[i+1]]
        d[r[i+1]] += 1
    print(ans)



        


if __name__ == '__main__':
    main()
1
