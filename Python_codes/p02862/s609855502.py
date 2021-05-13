# Combination
MOD = 10**9+7
MAX = 10**6+3
fac = [1,1] + [0]*MAX
finv = [1,1] + [0]*MAX
inv = [0,1] + [0]*MAX
for i in range(2,MAX+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def comb(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD

X, Y = map(int, input().split())
p1, p2 = -1, -1
for i in range(10**6+1):
    x, y = X-i, Y-2*i
    if x < 0 or y < 0: continue
    if x%2 == 0:
        q = x//2
        if y == q:
            p1, p2 = i, q
if p1 == -1:
    print(0)
else:
    print(comb(p1+p2, p1))