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
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()
    if len(t) == len(s) +1:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
