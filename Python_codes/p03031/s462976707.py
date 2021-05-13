import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    n,m = map(int, input().split())
    ans = 0
    S = []
    for i in range(m):
        s = list(map(int, input().split()))
        k = s.pop(0)
        S.append(s)
    p = list(map(int, input().split()))

    for i in range(1<<n):
        ok = True
        for j in range(m):
            cnt = 0
            for s in S[j]:
                if ((i>>s-1)&1): # スイッチが対象であれば
                    cnt += 1
            if cnt%2!=p[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)




if __name__=="__main__":
    main()
