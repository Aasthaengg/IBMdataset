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
    ans = 0
    trial = 0
    t = h[0]
    for i in h[1:]:
        if t >= i:
            trial += 1
            ans = max(ans, trial)
            t = i
        else:
            trial = 0
            t = i
    print(ans)





if __name__=="__main__":
    main()
