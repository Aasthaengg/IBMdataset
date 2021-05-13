import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n = int(input())
    l = list(map(int, input().split()))
    k = l[0]
    for i in range(1,n):
        k = gcd(k,l[i])
    print(k)


if __name__=="__main__":
    main(
    )
