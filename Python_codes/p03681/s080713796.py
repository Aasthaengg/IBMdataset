n, m = map(int, input().split())
mod = 10**9+7
facs = [1] * (max(n,m)+1)
nfac = 1
for i in range(1, max(n,m)+1):
    nfac = nfac * i % mod
    facs[i] = nfac
if abs(n - m) <= 1:
    print((2 if n==m else 1) * (facs[n] * facs[m]) % mod)
else:
    print(0)