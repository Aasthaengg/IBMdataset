N = int(input())
A, B, C = [list(map(int, input().split())) for _ in range(3)]

for x in [A, B, C]:
	x.sort()

def bsr(a, v, lo=0, hi=None):
	if hi == None:
		hi = len(a) - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if v < a[mid]:
			hi = mid - 1
		else:
			lo = mid + 1
	return lo

bt = []
for b in B:
	bt += [max(0, (N - bsr(C, b)))]

for i in range(len(B) - 2, -1, -1):
	bt[i] += bt[i + 1]

r = 0
for ai, a in enumerate(A):
	bif = bsr(B, a)
	if bif < N:
		r += bt[bif]

print(r)
