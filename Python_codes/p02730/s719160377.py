import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    s = list(input().rstrip())
    n = len(s)
    k = s.copy()
    k.reverse()
    if k != s:
        print("No")
        exit()
    k = s[0:(n-1)//2]
    l = k.copy()
    l.reverse()
    if k != l:
        print("No")
        exit()
    k = s[(n-1)//2+1:]
    l = k.copy()
    if k != l:
        print("No")
        exit()
    print("Yes")

if __name__=="__main__":
    main()
