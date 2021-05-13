import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n,k = map(int, input().split())
    ans = 0
    mn = mx = 0
    for i in range(n+1):
        j = n-i
        mn += i
        mx += j
        if i+1 >= k:
            ans += mx-mn+1
    print(ans%(10**9+7))

if __name__=="__main__":
    main()
