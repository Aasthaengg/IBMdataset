from math import ceil
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

K = int(input())
L = list(map(int, input().split()))

maxr = 2
minr = 2
r = 0
for n in reversed(L):
    # [minr,maxr]にnの倍数があるか
    if ceil(maxr//n)*n >= minr:
        minr = ceil(minr/n)*n
        maxr = (maxr)//n*n+n-1
    else:
        print(-1)
        exit()

print(int(minr), maxr)
