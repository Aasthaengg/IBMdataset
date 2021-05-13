# 逆元を利用した組み合わせの計算
#############################################################


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


# 問題に応じて変える、素数の時しか動作しない
mod = 10**9 + 7
# 問題に応じて変える、上限
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
#####################################################

X, Y = map(int, input().split())

# X+Yが3の倍数のマスしか通りえない
if (X + Y) % 3 == 0:
    # (1,2)移動をn回、(2,1)移動をm回したとする
    # n+2m = X, 2n+m = Y
    # n,mについて解く
    n = (2 * Y - X) // 3
    m = (2 * X - Y) // 3

    if n >= 0 and m >= 0:
        print(cmb(n + m, n, mod))
    else:
        print(0)

# X+Yが3の倍数でない場合
else:
    print(0)
