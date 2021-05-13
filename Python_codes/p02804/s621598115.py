# 逆元を利用した組み合わせの計算
#############################################################
def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

N = 10**5
mod = 10**9 + 7

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
#############################################################

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

mod = 10**9 + 7
# Σf(X) = Σ(max(X)-min(X)) = Σmax(X) - Σmin(X) = ans1 - ans2
# ソートしておくことで、集合の最大値は右端の値、最小値は左端の値とすることが出来る
ans1 = 0
ans2 = 0
for i in range(1, N + 1):
    # A[i-1]の左にある(i-1)個の中から(K-1)個選ぶ
    ans1 += A[i-1]*cmb(i - 1, K - 1, mod)
    # A[i-1]の右にある(N-i)個の中から(K-1)個選ぶ
    ans2 += A[i-1]*cmb(N - i, K - 1, mod)

ans = (ans1 - ans2) % mod
print(ans)
