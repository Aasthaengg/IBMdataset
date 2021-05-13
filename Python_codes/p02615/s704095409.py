import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0 + a[-1]
    for i in range(n-2):
        k = a[-((i+4)//2)]
        ans += k
    print(ans)

if __name__=="__main__":
    main()
