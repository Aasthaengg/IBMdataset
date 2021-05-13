import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    d = int(input())
    d = math.radians(d)
    x = 0
    y = 1
    cnt = 1
    while True:
        if abs(x)<=0.001 and abs(y) <=0.001:
            print(cnt)
            exit()
        x -= math.sin(d*cnt)
        y += math.cos(d*cnt)
        cnt += 1

if __name__=="__main__":
    main()
