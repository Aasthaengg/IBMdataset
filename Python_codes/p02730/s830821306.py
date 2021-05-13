import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    s = list(input().rstrip())
    n = len(s)
    h = n//2
    f = s[:h]
    l = s[h+1:]
    if s == s[::-1] and f == f[::-1] and l == l[::-1]:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
