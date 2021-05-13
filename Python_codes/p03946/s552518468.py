from collections import defaultdict

N, T, *A = map(int, open(0).read().split())

ctr = defaultdict(int)
m = 10 ** 9 + 7
for i in range(N):
    m = min(m, A[i])
    ctr[A[i] - m] += 1

print(ctr[max(ctr)])
