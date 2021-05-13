import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    a,b,c,d = map(int, input().split())
    x = b//c - (a-1)//c
    y = b//d - (a-1)//d
    e = c*d//gcd(c,d)
    z = b//e - (a-1)//e
    ans = b-a+1 -x-y +z
    print(ans)

if __name__=="__main__":
    main()
