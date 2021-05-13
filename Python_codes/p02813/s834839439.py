import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    l = list(itertools.permutations(range(1,n+1)))
    print(abs(l.index(p) - l.index(q)))


if __name__=="__main__":
    main()
