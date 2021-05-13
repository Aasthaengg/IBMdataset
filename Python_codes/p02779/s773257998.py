import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = Counter(l)
    if all(i == 1 for i in l.values()):
        print("YES")
    else:
        print("NO")


if __name__=="__main__":
    main()
