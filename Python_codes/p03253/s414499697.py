N, M = map(int, input().split())
MOD = 10**9+7

def factorize(N):
    res = []
    for i in range(2, N):
        if i**2 > N: break
        if N % i != 0: continue
        num = 0
        while N % i == 0:
            N = int(N/i)
            num += 1
        res.append(num)
    if N>1: res.append(1)
    return res

res = factorize(M) if M>1 else [0]

n = max(res) + N 

fac = [1]*n
inv = [1]*n
finv = [1]*n

for i in range(2, n):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * int(MOD / i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

ans = 1
for m in res:
    a = fac[m+N-1] * (finv[m] * finv[N-1] % MOD) % MOD
    ans = ans*a%MOD

print(ans)