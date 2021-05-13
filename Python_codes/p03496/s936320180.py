import numpy as np
N = int(input())
a = np.array(list(map(int, input().split())))
a_max = a.max()
a_min = a.min()
if abs(a_max) >= abs(a_min):
	add_idx = a.argmax() + 1
else:
	add_idx = a.argmin() + 1
if a_max + a_min >= 0:
	rng_idx = range(1, N)
	sgn = 1
else:
	rng_idx = range(N, 1, -1)
	sgn = -1
print(2 * N - 1)
for i in range(1, N + 1):
	print(add_idx, i)
for i in rng_idx:
	print(i, i + sgn)
