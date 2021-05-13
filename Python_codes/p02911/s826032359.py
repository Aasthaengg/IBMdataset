import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n,k,q = map(int, input().split())
    ans = [k-q]*n
    for i in range(q):
        k = int(input())  - 1
        ans[k] += 1
    for i in ans:
        if i > 0:
            print("Yes")
        else:
            print("No")


if __name__=="__main__":
    main()
