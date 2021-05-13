import numpy as np
H,W,K = map(int, input().split())
C = np.array([list(map(int, input())) for _ in range(H)])
C = np.hstack([np.zeros([H,1]),C])
np.cumsum(C, axis=1, out=C)
ans = 10**5
for s in range(1<<(H-1)):
	ind = 0
	A = np.zeros([1,W+1])
	for i in range(H):
		if s >> i & 1 == 1:
			A = np.vstack([A,C[ind:i+1,:].sum(axis=0)])
			ind = i+1
	A = np.vstack([A,C[ind:].sum(axis=0)])

	ind = 0
	cnt = 0
	while True:
		cut = 10**3+2
		for a in A:
			cut = min(cut, np.searchsorted(a,a[ind]+K,side='right'))
		if cut == W+1:
			break
		if ind == cut-1:
			cnt = 10**4+2
			break
		else:
			ind = cut-1
		cnt += 1

	h_cnt = 0
	for i in range(H):
		if s >> i & 1 == 1:
			h_cnt += 1

	ans = min(ans, cnt+h_cnt)

print(ans)