import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    w,h,x,y = map(int, input().split())
    s = (w*h)/2
    if x*2 == w and y*2 == h:
        k = 1
    else:
        k = 0
    print(s,k)



if __name__=="__main__":
    main()
