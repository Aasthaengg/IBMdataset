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
    ans = sum(a)
    l = [0]*10**5
    for i in a:
        l[i-1] += 1
    q = int(input())
    for i in range(q):
        b,c = map(int, input().split())
        ans += (c-b)*l[b-1]
        l[c-1] += l[b-1]
        l[b-1] = 0
        print(ans)

if __name__=="__main__":
    main()
