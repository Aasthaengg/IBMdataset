import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():

    s = list(input().rstrip())
    zero = 0
    one = 0
    for i in s:
        if i == "0":
            zero += 1
        else:
            one += 1
    print(2*min(zero,one))

if __name__=="__main__":
    main()
