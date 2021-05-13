import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    a,b,n = map(int, input().split())

    k = min(n,b-1)
    print(math.floor(a*k/b) - a*math.floor(k/b))

if __name__=="__main__":
    main()
