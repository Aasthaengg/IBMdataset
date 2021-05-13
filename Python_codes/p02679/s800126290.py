from collections import defaultdict
from itertools import groupby, accumulate, product, permutations, combinations
from math import gcd

def reduction(x,y):
    g = gcd(x,y)
    return abs(x)//g,abs(y)//g

def solve():
    mod = 10**9+7
    dplus = defaultdict(lambda: 0)
    dminus = defaultdict(lambda: 0)
    N = int(input())
    xzero,yzero,xyzero = 0,0,0
    for i in range(N):
        x,y = map(int, input().split())
        if x==0:
            if y==0:
                xyzero += 1
            else:
                xzero += 1
        elif y==0:
            yzero += 1
        elif x*y>0:
            dplus[reduction(x,y)] += 1
        else:
            dminus[reduction(-y,x)] += 1
    ans = pow(2,xzero,mod)+pow(2,yzero,mod)-1
    other = N-xzero-yzero-xyzero
    for k,v in dplus.items():
        ans *= pow(2,dminus[k],mod)+pow(2,v,mod)-1
        other -= dminus[k]+v
    ans *= pow(2,other,mod)
    ans += xyzero-1
    ans %= mod
    return ans
print(solve())