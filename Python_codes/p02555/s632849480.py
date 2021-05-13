S = int(input())


def add(a, b, BIGMOD):
    return (a + b) % BIGMOD


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10 ** 9 + 7  # 出力の制限
Nn = 10 ** 6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, Nn + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

Sum = 0
MOD = 10 ** 9 + 7

for i in range(1, S // 3 + 1):
    if 3 * i <= S:
        Sum = add(Sum, cmb(S - 3 * i + (i - 1), i - 1, MOD), MOD)
print(Sum)