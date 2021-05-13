import sys
input = sys.stdin.readline
from collections import *
from math import gcd

N = int(input())
cnt = defaultdict(int)
abzero = 0
azero = 0
bzero = 0

for _ in range(N):
    A, B = map(int, input().split())
    
    if A==0 and B==0:
        abzero += 1
        continue
    elif A==0:
        azero += 1
        continue
    elif B==0:
        bzero += 1
        continue
        
    G = gcd(abs(A), abs(B))
    A //= G
    B //= G
    
    if (A<0 and B>0) or (A<0 and B<0):
        A *= -1
        B *= -1
    
    cnt[(A, B)] += 1

ans = 1
MOD = 10**9+7
visited = set()

for k in cnt.keys():
    if k in visited:
        continue
    
    if k[0]>0 and k[1]>0:
        k2 = (k[1], -k[0])
    else:
        k2 = (-k[1], k[0])
    
    if k2 not in cnt:
        ans *= pow(2, cnt[k], MOD)
        ans %= MOD
    else:
        ans *= pow(2, cnt[k], MOD)+pow(2, cnt[k2], MOD)-1
        ans %= MOD
        visited.add(k2)

ans *= pow(2, azero, MOD)+pow(2, bzero, MOD)-1
ans %= MOD
ans += abzero-1
ans %= MOD
print(ans)
