from math import gcd

n = int(input())
A = list(map(int, input().split()))
maxA = 10**6+5

def furui(x):
    memo = [0]*(x+1)
    primes = []
    for i in range(2, x+1):
        if memo[i]: continue
        primes.append(i)
        memo[i] = i
        for j in range(i*i, x+1, i):
            if memo[j]: continue
            memo[j] = i
    return primes

primes = furui(maxA)

c = [0]*maxA
for a in A: c[a] += 1

for p in primes:
    cnt = 0
    for i in range(p, maxA, p):
        cnt += c[i]
    if cnt >= 2:
        break
else:
    print('pairwise coprime')
    exit()

g = 0
for a in A:
    g = gcd(g, a)
if g == 1:
    print('setwise coprime')
else:
    print('not coprime')