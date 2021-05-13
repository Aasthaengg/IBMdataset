def make_array_for_comb(N, mod=10**9+7):
    fact = [1,1]
    fact_inv = [1,1]
    inv = [0,1]
    for i in range(2, N+1):
        
        fact.append((fact[-1]*i) % mod)
        
        # モジュラ逆数の性質
        inv.append((-inv[mod%i] * (mod//i)) % mod)
        fact_inv.append((fact_inv[-1]*inv[i]) % mod)
    
    return fact, fact_inv

def cmb(n, r, mod=10**9+7):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n-r] % mod

N, K = map(int,input().split())
A = list(map(int,input().split()))
mod=10**9+7
A.sort()
A_rev = A[::-1]
fact, fact_inv = make_array_for_comb(N=N, mod=mod)
f_max, f_min = 0, 0
for i, num in enumerate(A):
    if i >=K-1:
        f_max += num*cmb(i, K-1)
for i, num in enumerate(A_rev):
    if i >= K-1:
        f_min += num*cmb(i, K-1)
print((f_max - f_min)%mod)