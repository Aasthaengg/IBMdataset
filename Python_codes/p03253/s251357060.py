import math

def factorize(n):
    d = {}
    temp = int(math.sqrt(n))+1
    for i in range(2, temp):
        while n%i== 0:
            n //= i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    if d == {}:
        d[n] = 1
    else:
        if n in d:
            d[n] += 1
        elif n != 1:
            d[n] =1
    return d

n, m = map(int, input().split())

if m == 1:
    print(1)
    exit()

def cmb1(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7
N = 2*10**5+5
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

d = factorize(m)
ans = 1
for v in d.values():
    ans *= cmb1(v+n-1, v, mod)
    ans %= mod
print(ans%mod)
