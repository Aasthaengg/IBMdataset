import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n,m = map(int, input().split())
    dic = {}
    for i in range(1,n+1):
        dic[i] = 0
    ac = 0
    wa = 0
    for i in range(m):
        p,s = input().split()
        p = int(p)
        if dic[p] == 0: # その問題初めての投稿
            if s == "WA":
                dic[p] += 1
            else:
                dic[p] = "AC"
                ac += 1
        elif dic[p] == "AC":
            pass
        else: # WA状態
            if s == "WA":
                dic[p] += 1
            else:
                wa += dic[p]
                dic[p] = "AC"
                ac += 1
    print(ac,wa)



if __name__=="__main__":
    main()
