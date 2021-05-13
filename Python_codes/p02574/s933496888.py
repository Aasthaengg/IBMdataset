from math import gcd

"""
pairwise coprimeであるための条件は、全てのAに関して素因数に重複がないことである。
したがって、各Aに関して素因数分解を行う⇒各数の素因数の種類数をカウントし総和する。⇒全体の素因数の種類数をカウントし、先ほどの総和と比較する。
"""
N = int(input())
A = list(map(int,input().split()))
primes = []
def primeFinder(n):
    memo = [1]*(n+1)
    memo[0] = 0
    memo[1] = 0
    for i in range(2,n+1):
        if memo[i] == 1:
            primes.append(i)
            for j in range(i*2,n+1,i):
                memo[j] = 0
primeFinder(1000000)

primeMemo = set()
cnt = 0
for i in range(N):
    a = A[i]
    for p in primes:
        if p*p > a:
            break
        if a%p == 0:
            cnt += 1
            primeMemo.add(p)
        while a%p==0:
            a //= p
    if a != 1:
        cnt += 1
        primeMemo.add(a)

if cnt == len(primeMemo):
    print('pairwise coprime')
    exit()
g = A[0]
for i in range(1,N):
    g = gcd(g,A[i])
if g == 1:
    print('setwise coprime')
else:
    print('not coprime')