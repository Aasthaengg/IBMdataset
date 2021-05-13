import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        k = input().rstrip()
        dic[k] = dic.get(k,0) + 1

    m = max(list(dic.values()))
    ans = []
    for i,k in dic.items():
        if k == m:
            ans.append(i)
    print("\n".join(sorted(ans)))




if __name__=="__main__":
    main()
