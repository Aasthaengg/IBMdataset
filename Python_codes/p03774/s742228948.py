import math
import collections
from sys import exit
from itertools import product

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,m  = mi()
ab = [li() for _ in range(n)]
cd = [li() for _ in range(m)]

for i in range(n):
    length = 10**10
    ans = 0
    for j in range(m):
        if abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1]) < length:
            length = abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
            ans = j
    print(ans+1)