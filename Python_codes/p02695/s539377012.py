import sys
from itertools import combinations_with_replacement as comb

N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

Max = 0

for A in comb(range(1, M + 1), N):
    score = 0
    for j in range(Q):
        if (A[b[j] - 1] - A[a[j] - 1]) == c[j]:
            score += d[j]

    Max = max(Max, score)

print(Max)
