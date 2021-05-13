import numpy as np
import sys
from numba import njit, i8

mod = 10 ** 9 + 7
@njit((i8, i8, i8[:]), cache=True)
def main(n, k, a):
	fac = np.full(n + 3, 1, dtype = np.int64)
	for i in range(1, n + 1):
		fac[i] = fac[i - 1] * i % mod
	
	def inv(x):
		res = 1
		e = mod - 2
		while e > 0:
			if e & 1:
				res = res * x % mod
			x = x * x % mod
			e >>= 1
		return res
	def c(n, k):
		return fac[n] * inv(fac[n - k] * fac[k] % mod) % mod

	ans = 0
	for i in range(n - k + 1):
		ans += (a[n - 1 - i] - a[i]) * c(n - 1 - i, k - 1)
		ans %= mod
	print(ans)


if __name__ == '__main__':
	stdin = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
	n, k = stdin[:2]
	a = np.sort(stdin[2:])
	main(n, k, a)
