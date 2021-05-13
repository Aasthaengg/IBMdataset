k = int(input())
s = input()
n = len(s)

mod = 10 ** 9 + 7
N = 2 * 10 ** 6 + 10

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

dpi = 1

memo = [1]
for i in range(N):
    memo.append(memo[-1]*25 % mod)

for i in range(1, k+1):
    dpi = (dpi * 26) % mod + (cmb(n+i-1,n-1) * memo[i]) % mod
    dpi %= mod

print(dpi)