def nCr(n, r, mod):
    x, y = 1, 1
    for r_ in range(1, r+1):
        x = x*(n+1-r_)%mod
        y = y*r_%mod
    return x*pow(y, mod-2, mod)%mod

n, k = map(int, input().split())
mod = 10**9+7
for i in range(1, k+1): print(nCr(n-k+1, i, mod)*nCr(k-1, i-1, mod)%mod)