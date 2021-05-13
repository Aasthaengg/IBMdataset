from math import factorial
N, K = map(int, input().split())

# 逆元を利用した組み合わせの計算
#############################################################
def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10**9 + 7
NN = 2200

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, NN + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
#############################################################
"""
x_1 + x_2 + ... x_k = n
x_i >= 0
k個の箱にn個のボールを入れる重複組み合わせ　n+k-1_C_k-1
n個の玉とk-1個の仕切りを並べる

x_1 + x_2 + ... x_k = n
x_i >= 1
k個の箱にn個のボールを1個以上入れる重複組み合わせ　n-1_C_k-1
n個の玉の仕切りn-1個の中に、k-1箇所仕切りを入れる
"""

"""
まず赤だけ並べ、赤の間、左端、右端のN-K+1箇所から、i箇所を選ぶ -> N-K+1_C_i
選んだi箇所について、青を1個以上配置する -> 青の間K-1箇所からi-1箇所選ぶ -> K-1_C_i-1
"""

# i = 1,2,...,K
for i in range(1, K + 1):
    # まず赤だけ並べ、赤の間、左端、右端のN-K+1箇所から、i箇所を選ぶ
    c1 = cmb(N - K + 1, i, mod)
    # i箇所について、青を1個以上配置する、青の間K-1箇所からi-1個選ぶ
    c2 = cmb(K - 1, i - 1, mod)

    ans = (c1 * c2) % mod
    print(ans)
