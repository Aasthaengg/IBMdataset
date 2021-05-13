import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    a,b = map(int, input().split())
    ans = max(a,b)
    first = ans
    m = min(a,b)
    while True:
        if ans%m == 0:
            print(ans)
            exit()
        ans += first

if __name__=="__main__":
    main()
