import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n, k =  map(int, input().split())
    ans = 0

    for i in range(1, n+1):
        for j in range(100):
            if i*2**j >= k:
                ans += 0.5**j
                break
    print((1/n)*ans)


if __name__=="__main__":
    main()
