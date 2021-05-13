import numpy as np
n, k, q = map(int, input().split())
A = np.array([int(input()) - 1 for _ in range(q)])
score = np.zeros(n)
for i in A:
    score[i] += 1
score = k + score - q
print(*np.where(score > 0, 'Yes', 'No'), sep='\n')
