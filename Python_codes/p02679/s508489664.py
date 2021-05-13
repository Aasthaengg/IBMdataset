import sys
input = sys.stdin.readline
from collections import *

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
zero1 = 0
zero2 = 0
zero3 = 0
cnt = defaultdict(int)
MOD = 10**9+7

for _ in range(N):
    A, B = map(int, input().split())
    
    if A==0 and B==0:
        zero1 += 1
    elif A>0 and B>0:
        G = gcd(A, B)
        A //= G
        B //= G
        cnt[(A, B)] += 1
    elif A>0 and B<0:
        B *= -1
        G = gcd(A, B)
        A //= G
        B //= G
        cnt[(-A, B)] += 1
    elif A<0 and B>0:
        A *= -1
        G = gcd(A, B)
        A //= G
        B //= G
        cnt[(-A, B)] += 1
    elif A<0 and B<0:
        A *= -1
        B *= -1
        G = gcd(A, B)
        A //= G
        B //= G
        cnt[(A, B)] += 1
    elif A==0:
        zero2 += 1
    elif B==0:
        zero3 += 1

s = set()
ans = 1

for k in cnt.keys():
    if k in s:
        continue
    
    k2 = (-k[1], k[0])
    
    if k2[0]<0 and k2[1]<0:
        k2 = (-k2[0], -k2[1])
        
    a = cnt[k]
    
    if k2 not in cnt:
        ans *= pow(2, a, MOD)
        ans %= MOD
    else:
        b = cnt[k2]
        ans *= pow(2, a, MOD)+pow(2, b, MOD)-1
        ans %= MOD
        s.add(k2)

ans *= pow(2, zero2, MOD)+pow(2, zero3, MOD)-1
ans += zero1
ans %= MOD
ans -= 1
ans %= MOD

print(ans)
