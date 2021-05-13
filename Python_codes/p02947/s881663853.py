import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    s = [sorted(list(input().rstrip())) for _ in range(n)]
    s.sort()

    ans = 0
    trial = s[0]
    tri_num = 0
    for i in s[1:]:
        if trial == i:
            tri_num += 1
        else:
            ans += tri_num*(tri_num+1)//2
            tri_num = 0
            trial = i
    if tri_num != 0:
        ans += tri_num*(tri_num+1)//2
    print(ans)

if __name__=="__main__":
    main()
