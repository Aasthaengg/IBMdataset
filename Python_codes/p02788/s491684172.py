import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, D, A = map(int, input().split())

I = np.array(read().split(), np.int64)
X = I[::2]
H = I[1::2]

sort_ind = np.argsort(X)
X = X[sort_ind]
H = H[sort_ind]

atack = np.zeros(N+1, np.int64)
cover = np.searchsorted(X, X + (2 * D), side = 'right')

ans = 0
cnt = 0
for i in range(N):
	cnt += atack[i]
	H[i] -= cnt
	if H[i] > 0:
		tmp = -(-H[i]//A)
		ans += tmp
		cnt += tmp * A
		atack[cover[i]] -= tmp * A

print(ans)