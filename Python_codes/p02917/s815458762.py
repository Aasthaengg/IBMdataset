import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    b = list(map(int, input().split()))
    b.insert(0,INF)
    b.append(INF)
    ans = []
    for i in range(len(b)-1):
        ans.append(min(b[i],b[i+1]))
    print(sum(ans))


if __name__=="__main__":
    main()
