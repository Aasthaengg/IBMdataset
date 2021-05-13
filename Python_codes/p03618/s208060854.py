from collections import defaultdict as dd
A = input()
N = len(A)
d = dd(int)
for i in range(N):
	d[A[i]] += 1
cnt = 0
for v in d.values():
	cnt += v*(v-1)//2
print(N*(N-1)//2 - cnt + 1)