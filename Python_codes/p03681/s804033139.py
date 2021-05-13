from math import factorial as frac

N, M = map(int, input().split())

MOD = 10**9 + 7

def nPk(n, k):
    r = 1
    while k > 0:
        r *= n
        r %= MOD
        n -= 1
        k -=  1
    return r

if abs(N-M) > 1:
    print(0)
elif N==M:
    print(((nPk(N,N)*nPk(M,M))*2)%MOD)
else:
    print(nPk(N,N)*nPk(M,M)%MOD)
