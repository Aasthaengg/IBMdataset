k = int(input())
s = input()
mod = 10**9+7

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

modp = mod
max_n = k + len(s)+1 # 必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod modp)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod modp)
inv = [0, 1]  # factinv 計算用

for i in range(2, max_n + 1):
    fact.append((fact[-1] * i) % modp)
    inv.append((-inv[modp % i] * (modp // i)) % modp)
    factinv.append((factinv[-1] * inv[-1]) % modp)

ans = 0
for i in range(k+1):
    now = pow(26, k-i, mod)
    now = (now * pow(25, i, mod))%mod
    now = (now * cmb(i+len(s)-1, len(s)-1, mod))%mod
    ans += now
print(ans%mod)