import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n = int(input())
    h = list(map(int, input().split()))
    l = [[0]*100 for _ in range(100)]
    for i in range(len(h)):
        k = h[i]
        for q in range(k):
            l[i][q] = 1
    l = [list(x) for x in zip(*l)]
    ans = 0
    for i in l:
        flg = 0
        for g in i:
            if g == 1:
                if flg == 0:
                    ans += 1
                flg = 1
            if g == 0:
                flg = 0
    print(ans)


if __name__=="__main__":
    main()
