import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    m = max(a)
    s = sorted(a)[-2]
    for i in a:
        if i == m:
            print(s)
        else:
            print(m)

if __name__=="__main__":
    main()
