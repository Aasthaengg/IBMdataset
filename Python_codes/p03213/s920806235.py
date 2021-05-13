from collections import defaultdict as dd
from itertools import permutations as p

def factorize(n):
    d = dd(int)
    for i in range(2, int(n**0.5)+1):
        while n%i==0:
            d[i] += 1
            n //= i
        if not n:
            break
    if n>1:
        d[n] += 1
    return d

N = int(input())
d = dd(int)
for i in range(1, N+1):
    e = factorize(i)
    for i,j in e.items():
        d[i] += j

ans = 0
for i, j, k in p(d.values(), 3):    
    if i>=2 and j>=4 and k>=4:
        ans += 1
ans //= 2

for i, j in p(d.values(), 2):
    if i>=2 and j>=24:
        ans += 1
    if i>=4 and j>=14:
        ans += 1

for i in d.values():
    if i>=74:
        ans += 1

print(ans)