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
    #print("max={}min={}".format(maxr, minr))
    if ceil(maxr//n)*n >= minr:
        # if any(x % n == 0 for x in range(minr, maxr+1)):
        # if minr//n <= maxr//n:
        minr = ceil(minr/n)*n
        maxr = (maxr)//n*n+n-1
    else:
        n = -1
        break

if n == -1:
    print(n)
else:
    print(int(minr), maxr)
