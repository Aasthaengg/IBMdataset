from math import gcd
MAX = 10**6

sieve = [i for i in range(MAX+1)]

p = 2
while p * p <= MAX:
    if sieve[p] == p:
        for i in range(p*2, MAX+1, p):
            if sieve[i] == i:
                sieve[i] = p
    p += 1


N = int(input())
A = list(map(int, input().split()))
pf = []

for a in A:
    tmp = set()
    b = a
    while b != 1:
        tmp.add(sieve[b])
        b //= sieve[b]
    pf.append(tmp)


soin = [0] * (10 ** 6 + 1)
for f in pf:
    for n in f:
        soin[n] += 1

if max(soin[2:]) <= 1:
    print('pairwise coprime')
    exit()


setwise = A[0]

for a in A:
    setwise = gcd(setwise, a)
    
if setwise == 1:
    print('setwise coprime')
else:
    print('not coprime')