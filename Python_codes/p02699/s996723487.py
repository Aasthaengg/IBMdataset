import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    s,w = map(int, input().split())
    if w>=s:
        print("unsafe")
    else:
        print("safe")

if __name__=="__main__":
    main()
