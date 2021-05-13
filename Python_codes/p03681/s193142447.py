N,M=map(int,input().split())

if abs(N-M)>1:
    print(0)
    exit()

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
n = 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p) 階乗のmod
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans=(fact[N]*fact[M])%p
if N==M:
    ans*=2
    ans%=p
print(ans)