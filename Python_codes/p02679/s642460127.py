import sys
input = sys.stdin.readline
from collections import *
from math import gcd

N = int(input())
zerozero = 0
zero1 = 0
zero2 = 0
cnt = defaultdict(int)

for _ in range(N):
    A, B = map(int, input().split())
    
    if A==0 and B==0:
        zerozero += 1
    elif A==0:
        zero1 += 1
    elif B==0:
        zero2 += 1
    else:
        G = gcd(abs(A), abs(B))
        A //= G
        B //= G
        
        if (A<0 and B<0) or (A<0 and B>0):
            cnt[(-A, -B)] += 1
        else:
            cnt[(A, B)] += 1

ans = 1
MOD = 10**9+7
checked = set()

for k, v in cnt.items():
    if k in checked:
        continue
    
    if k[0]>0 and k[1]>0:
        k2 = (k[1], -k[0])
    else:
        k2 = (-k[1], k[0])
    
    if k2 in cnt:
        v2 = cnt[k2]
        ans *= pow(2, v, MOD)+pow(2, v2, MOD)-1
        ans %= MOD
        checked.add(k2)
    else:
        ans *= pow(2, v, MOD)
        ans %= MOD

ans *= pow(2, zero1, MOD)+pow(2, zero2, MOD)-1
ans %= MOD
ans += zerozero
ans %= MOD
print((ans-1)%MOD)