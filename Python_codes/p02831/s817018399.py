import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    a,b = map(int, input().split())
    print(int(a*b/gcd(a,b)))

if __name__=="__main__":
    main()
