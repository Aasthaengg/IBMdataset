import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    mid = n//2-1
    left = d[mid]
    right = d[mid+1]
    print(right-left)


if __name__=="__main__":
    main()
