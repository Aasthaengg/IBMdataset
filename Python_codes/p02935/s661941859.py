import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v)>1:
        a = v[0]
        b = v[1]
        c = (a+b)/2
        v.pop(0)
        v.pop(0)
        v.insert(0, c)
    print(v[0])


if __name__=="__main__":
    main()
