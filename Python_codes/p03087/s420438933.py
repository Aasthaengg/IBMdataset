import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n,q = map(int, input().split())
    s = input().rstrip()
    t = [0]*(n+1)
    for i in range(n):
        if s[i:i+2] == "AC":
            t[i+1] = t[i] + 1
        else:
            t[i+1] = t[i]

    for i in range(q):
        l,r = map(int, input().split())
        print(t[r-1] - t[l-1])

if __name__=="__main__":
    main()
