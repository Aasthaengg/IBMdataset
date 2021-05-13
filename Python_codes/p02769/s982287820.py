n, k = map(int, input().split())

mod = 10 ** 9 + 7
N = 10 ** 6

#逆元テーブル
inv_t = [0]+[1]
for i in range(2, N):
  inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

#階乗計算
kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
	kai.append(kai[-1] * i % mod)
	rev_kai.append(rev_kai[-1] * inv_t[i] % mod)

# コンビネーション計算
def cmb(n, r):
	return kai[n] * rev_kai[r] * rev_kai[n-r] % mod

ans = 0
for i in range(0, min(k+1, n)):
    ans += cmb(n, i) * cmb(n-1, i) % mod
    ans %= mod
print(ans)
