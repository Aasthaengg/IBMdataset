# 隣り合うブロックの組で色が異なるものがk(0,1,2,...,K)個とする。
# (左端の色) × (2~N番目のうち、どのk箇所を選ぶか) × (2~N番目の色)
# = M * N-1_C_k * (M-1)**(N-k-1)

from math import factorial
N, M, K = map(int, input().split())
p = 998244353

####################################################
# 逆元を用いた組み合わせの計算用


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
####################################################
ans = 0

for k in range(K + 1):
    tmp = M * cmb(N - 1, k, p) * pow(M - 1, N - k - 1, p)
    ans += tmp % p

ans = ans % p
print(ans)
