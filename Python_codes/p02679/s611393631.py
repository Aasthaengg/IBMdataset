import sys
input = sys.stdin.readline
from math import gcd
def solve():
    N = int(input())
    AB = [tuple(map(int,input().split())) for i in range(N)]
    MOD = 10**9+7

    from collections import Counter
    ctr = Counter()
    az = bz = zz = 0
    for a,b in AB:
        if a==b==0:
            zz += 1
        elif a==0:
            az += 1
        elif b==0:
            bz += 1
        else:
            g = gcd(a,b)
            a,b = a//g, b//g
            if b < 0:
                b *= -1
                a *= -1
            ctr[(a,b)] += 1
    ans = pow(2,az,MOD) + pow(2,bz,MOD) - 1

    used = set()
    for (a1,b1),v in ctr.items():
        if (a1,b1) in used: continue
        a2,b2 = -b1,a1
        if b2 < 0:
            b2 *= -1
            a2 *= -1
        if (a2,b2) in ctr:
            used.add((a2,b2))
        r = pow(2,v,MOD) + pow(2,ctr[(a2,b2)],MOD) - 1
        ans *= r
        ans %= MOD
    ans += zz - 1
    ans %= MOD
    print(ans)
solve()