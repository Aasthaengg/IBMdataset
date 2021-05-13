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
    ans = [0]*(n+1)
    b = list(map(int, input().split()))
    for i in range(n):
        if a[i]-ans[i] >= b[i]:
            ans[i] += b[i]
        else:
            k = ans[i]
            ans[i] += a[i]-k
            rest = b[i] - a[i] + k
            ans[i+1] += min(rest,a[i+1])
    print(sum(ans))

if __name__=="__main__":
    main()
