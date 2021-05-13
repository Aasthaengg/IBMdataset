from math import gcd
N = int(input())
A = list(map(int,input().split()))

g = 0
for a in A:
    g = gcd(g,a)
if g > 1:
    print('not coprime')
    exit()

MAXN = 10**6+10
sieve = [i for i in range(MAXN+1)]
p = 2
while p*p <= MAXN:
    if sieve[p] == p:
        for q in range(2*p,MAXN+1,p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

st = set()
for a in A:
    tmp = set()
    while a > 1:
        tmp.add(sieve[a])
        a //= sieve[a]
    for p in tmp:
        if p in st:
            print('setwise coprime')
            exit()
        st.add(p)
print('pairwise coprime')