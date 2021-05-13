K, N, *A = map(int, open(0).read().split())
A = [A[-1] - K] + A

max_gap = 0
for a1, a2 in zip(A, A[1:]):
    max_gap = max(max_gap, a2 - a1)
print(K - max_gap)
