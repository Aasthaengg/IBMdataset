import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]

    l.sort()
    ans = 0
    for i in l:
        if m<=i[1]:
            ans += m*i[0]
            break
        else:
            ans += i[0]*i[1]
            m -= i[1]
    print(ans)

if __name__=="__main__":
    main()
