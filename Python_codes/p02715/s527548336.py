from math import gcd
import sys
input = sys.stdin.readline

mod = 1000000007


def fpow(x, power, mod):
    x %= mod
    ans = 1
    while power != 0:
        if (power & 1) == 1:
            ans = ans * x % mod
        power >>= 1
        x = x * x % mod
    return ans


def fac(x):
    A = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            A.append(i)
            if (x // i) != i:
                A.append(x // i)
        i += 1
    return A


n, k = map(int, input().split())
ans = 0
# print(fpow(n,k,mod))
A = [0] * (k + 2)
ans = 0
for i in range(k, 0, -1):
    #print(i,A[i],fpow(k // i, n, mod))
    A[i] += fpow(k // i, n, mod)
    while A[i] < 0:
        A[i] += mod
    A[i] %= mod
    ans = ans + A[i] * i
    ans %= mod
    B = fac(i)
    for b in B:
        if b!=i:
            A[b] -= A[i]

print(ans)
