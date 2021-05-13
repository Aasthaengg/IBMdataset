#cited from maspy
import itertools
import numpy as np

N, M, Q = map(int, input().split())
A = np.array(list(itertools.combinations_with_replacement(range(1, M + 1), N)))
n = len(A)
score = np.zeros(n, np.int32)
m = [list(map(int, input().split())) for i in range(Q)]
for a, b, c, d in m:
    cond = A[:, b - 1] - A[:, a - 1] == c
    score += d * cond
print(score.max())