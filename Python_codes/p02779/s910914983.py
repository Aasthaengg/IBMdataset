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
    len_l = len(l)
    len_set_l = len(set(l))
    if len_l != len_set_l:
        print("NO")
    else:
        print("YES")



if __name__=="__main__":
    main()
