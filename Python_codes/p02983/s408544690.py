import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    l,r = map(int, input().split())
    if r-l > 2019:
        print(0)
        exit()
    ans = []
    for i in range(l,r+1):
        ans.append(i%2019)
    p = []
    ans = list(itertools.combinations(ans, 2))
    for k in ans:
        c = k[0]*k[1]
        p.append(c%2019)
    print(min(p))

if __name__=="__main__":
    main()
