import sys
input = sys.stdin.readline
K = int(input())
N = len(input().rstrip())
mod = 10**9 + 7
pow25 = [1]
pow26 = [1]
x = 1
y = 1
for i in range(K):
    x *= 25
    y *= 26
    x %= mod
    y %= mod
    pow25.append(x)
    pow26.append(y)

def comb(n, r, mod):
    if r<0 or r>n:
        return 0
    r = min(r, n-r)
    return fac[n] * (finv[r] * finv[n-r] % mod) % mod

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, N + K + 1):
    fac.append((fac[-1] * i) % mod)
    inv.append((-inv[mod%i] * (mod//i)) % mod)
    finv.append((finv[-1] * inv[-1]) % mod)

ans = 0
for i in range(K+1):
    ans += (((comb(i+N-1, N-1, mod) * pow25[i]) % mod) * pow26[K-i]) % mod
print(ans%mod)