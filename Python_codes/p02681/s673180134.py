import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
import string

def main():
    s = input().rstrip()
    t = input().rstrip()
    t = t[0:-1]
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
