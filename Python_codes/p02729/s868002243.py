import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n, m = map(int , input().split())
    a = len(list(itertools.combinations(list(range(n)), 2)))
    a += len(list(itertools.combinations(list(range(m)), 2)))
    print(a)


if __name__=="__main__":
    main()
