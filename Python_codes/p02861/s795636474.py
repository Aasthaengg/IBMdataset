import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n = int(input())
    path = list(itertools.permutations(list(range(n))))
    path_len = len(path)
    place = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in path:
        q = 0
        for k in range(n-1):
            q += ( (place[i[k+1]][0] - place[i[k]][0])**2 + (place[i[k+1]][1] - place[i[k]][1])**2 )**(1/2)
        ans += q
    print(ans/path_len)


if __name__=="__main__":
    main()
