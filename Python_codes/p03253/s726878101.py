import math

# 逆元を利用した組み合わせの計算
#############################################################
def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10**9 + 7
N = 10**6

# 元テーブル
g1 = [1, 1]
# 逆元テーブル
g2 = [1, 1]
# 逆元テーブル計算用テーブル
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
#############################################################

# Nの素因数分解を辞書で返す
#############################################################
def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict
#############################################################

N, M = map(int, input().split())
# Mを素因数分解
prime = prime_fact(M)
ans = 1
# Mがある素数pをv個持っていたとする
# a_1, ..., a_N に ちょうどv個を分配する
# v個のボールとN-1本の仕切りの並べ方に相当し、これは (N+v-1)_C_v 通り
for v in prime.values():
    ans *= cmb(N + v - 1, v, mod)
    ans %= mod
print(ans)
