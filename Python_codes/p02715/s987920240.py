import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
mod = 10**9+7
N, K = map(int, input().split())
ans = 0
cnt = np.zeros(K+1, np.int64)
for X in reversed(range(1,K+1)):
	a = K // X
	cnt[X] = pow(a,N,mod)
	x = 2
	res = 0
	while True:
		tmp = X * x
		if tmp > K:
			break
		res += cnt[tmp]
		res %= mod
		x += 1

	cnt[X] -= res
	cnt[X] %= mod
	ans += cnt[X] * X
	ans %= mod

print(ans)