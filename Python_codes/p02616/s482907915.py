import sys
from math import log

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def modinv(x, mod):
    a, b = x, mod
    u, v = 1, 0
    while b:
        t = a // b
        a -= t * b; a, b = b, a
        u -= t * v; u, v = v, u
    return u % mod


def solve():
    mod = 10**9 + 7
    n, k = nm()
    a = nl()
    a.sort(key=abs, reverse=True)

    if max(a) <= 0 or n == k:
        if k & 1:
            b = a[-k:]
        else:
            b = a[:k]
        d = 1
        for x in b:
            d = d * x % mod
        print(d)
        return

    d = 1
    for x in a[:k]:
        d = d * x % mod
    g = [x < 0 for x in a]

    if sum(g[:k]) % 2 == 0:
        print(d)
        return

    b = list(map(lambda x:-10000 if x == 0 else log(abs(x)), a))
    mpi = mmi = -1
    Mpi = Mmi = -1
    for i in range(k):
        if a[i] <= 0:
            mmi = i
        if a[i] >= 0:
            mpi = i
    for i in range(n-1, k-1, -1):
        if a[i] <= 0:
            Mmi = i
        if a[i] >= 0:
            Mpi = i
    if (mpi == -1 or Mmi == -1) and (mmi == -1 or Mpi == -1):
        if 0 in a: d = 0
    elif (mpi == -1 or Mmi == -1):
        d = d * a[Mpi] * modinv(a[mmi], mod) % mod
    elif (mmi == -1 or Mpi == -1):
        d = d * a[Mmi] * modinv(a[mpi], mod) % mod
    else:
        if a[Mpi] * a[mpi] >= a[Mmi] * a[mmi]:
            d = d * a[Mpi] * modinv(a[mmi], mod) % mod
        else:
            d = d * a[Mmi] * modinv(a[mpi], mod) % mod
    print(d)

    return

solve()
