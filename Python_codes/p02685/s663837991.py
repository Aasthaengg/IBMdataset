MOD = 998244353
MAX = 510000
fac = [1,1] # factorial
finv = [1,1] # inverse of factorial
inv = [None, 1] # inverse

def comb_init():
	for i in range(2, MAX):
		fac.append(fac[i-1] * i % MOD)
		inv.append(MOD - inv[MOD % i] * (MOD//i) % MOD)
		finv.append(finv[i-1] * inv[i] % MOD)

def inverse_mod(a):
	""" Calculate inverse of the integer in a modulo MOD """
	return pow(a, MOD-2, MOD)

def comb_mod(n, r):
	""" Calculate nCr modulo MOD. """
	if n < r: return 0
	if n < 0 or r < 0: return 0
	return fac[n]* (finv[r]*finv[n-r] % MOD) % MOD

def solve(n, m, k):
	ans = 0
	for k in range(K+1):
		ans = (ans + m*(comb_mod(n-1,k)*pow(m-1, n-k-1, MOD) % MOD) % MOD) % MOD
	return ans

comb_init()
N, M, K = map(int, input().split())
print(solve(N, M, K))
