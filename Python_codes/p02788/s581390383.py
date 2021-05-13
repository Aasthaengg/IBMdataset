import numpy as np
import sys
N, D, A = map(int, input().split())
L = 2 * D
I = np.array(sys.stdin.read().split(), np.int64)
X = I[::2]
H = I[1::2]
sort_ind = np.argsort(X)
X = X[sort_ind]
H = H[sort_ind]
S = np.zeros(N+1, np.int64)
ind = np.searchsorted(X,X+L+1,side = 'left')

atack = 0
ans = 0
for i in range(N):
	atack += S[i]
	H[i] -= atack
	if H[i] > 0:
		atack_cnt = -(-H[i]//A)
		ans += atack_cnt
		tmp = atack_cnt * A
		S[i+1] += tmp
		S[ind[i]] -= tmp

print(ans)