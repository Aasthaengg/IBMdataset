n,k = map(int,input().split())
"""
BBBBRBBBRBBRB
など.
Rで区切ればよい.
すなわち, R := 区切り棒, B := 自由
として, 自由の島が何個あるかを調べる.
"""
def cmb(n, r, mod):
	if (r < 0) or (n < r):
		return 0
	r = min(r, n-r)
	return fact[n]*factinv[r]*factinv[n-r]%mod


mod = 10**9+7
N = 10**4  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N+1):
	fact.append((fact[-1]*i)%mod)
	inv.append((-inv[mod%i]*(mod//i))%mod)
	factinv.append((factinv[-1]*inv[-1])%mod)

"""
わかった！！
N-K個の赤いボールに、「島」i個をならべて、
島の作り方でまた数え上げればいいんだ！
n-k個, i個, なので, cmb(n-k+i, i)でできそう.
そして島の作り方は, iは1個消費するので, 「区別ない」k-i個のボールを「区別ある」i個の島に分ける.
すなわち, cmb(k-i+i-1, k-i) = cmb(k-1, k-i)

よって cmb(n-k+1, i) * cmb(k-1, k-i)
"""

for i in range(1, k+1):
	print((cmb(n-k+1, i, mod)*cmb(k-1, k-i, mod))%mod)