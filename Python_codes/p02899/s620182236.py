import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    a = list(map(int , input().split()))
    ans = [0]*n
    for i, num in enumerate(a):
        ans[num-1] = i+1
    print(" ".join(map(str,ans)))

if __name__=="__main__":
    main()
