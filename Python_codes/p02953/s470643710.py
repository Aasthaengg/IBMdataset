import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    h = list(map(int, input().split()))
    k = h[0] - 1
    for i in h[1:]:
        if i < k: # 減少
            print("No")
            exit()
        if i == k:
            pass
        else:
            k = i - 1
    print("Yes")

if __name__=="__main__":
    main()
