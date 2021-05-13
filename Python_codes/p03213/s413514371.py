from collections import *

def factorize(n):
    fct = []
    
    for i in range(2, int(n**0.5)+1):
        c = 0
        
        while n%i==0:
            n //= i
            c += 1
        
        if c>0:
            fct.append((i, c))

    if n!=1:
        fct.append((n, 1))
    
    return fct

N = int(input())
cnt = defaultdict(int)

for i in range(1, N+1):
    fct = factorize(i)
    
    for p, c in fct:
        cnt[p] += c

c2, c4, c14, c24, c74 = 0, 0, 0, 0, 0

for v in cnt.values():
    if v>=2:
        c2 += 1
        
    if v>=4:
        c4 += 1
        
    if v>=14:
        c14 += 1
        
    if v>=24:
        c24 += 1
        
    if v>=74:
        c74 += 1

print(c74+c4*max(0, c4-1)//2*max(0, c2-2)+c24*max(0, c2-1)+c14*max(0, c4-1))