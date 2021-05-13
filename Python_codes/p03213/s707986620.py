import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())

primes = [0]*100
def prime_factorize(n):
    while n % 2 == 0:
        primes[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        primes[n] += 1

for i in range(1, N+1):
    prime_factorize(i)

up2 = 0
up4 = 0
up24 = 0
up14 = 0
up74 = 0
for i, p in enumerate(primes):
    if p>=2:
        up2 += 1
    if p>=4:
        up4 += 1
    if p>=24:
        up24 += 1
    if p>=14:
        up14 += 1
    if p>=74:
        up74 += 1

ans = 0
if up4>=2:
    ans += (up2-2)*(up4*(up4-1)//2)
if up24>=1:
    ans += (up2-1)*up24
if up14>=1:
    ans += (up4-1)*up14
if up74>=1:
    ans += up74

print(ans)
    
    
