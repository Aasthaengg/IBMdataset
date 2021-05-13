import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    ans = n - 1
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i == 0:
            ans = i-1 + n//i-1
    print(ans)

if __name__=="__main__":
    main()
