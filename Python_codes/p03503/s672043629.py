import numpy as np
n = int(input())
timezones = np.array([[int(i) for i in input().split()] for _ in range(n)])
points = np.array([[int(i) for i in input().split()] for _ in range(n)])
max_scores = - float('inf')
for i in range(1, 2 ** 10):
    indices = []
    for j in range(10):
        if i & (1 << j):
            indices.append(j)
    nums = timezones[:, indices].sum(axis=1)
    scores = points[range(n), nums].sum()
    max_scores = max(max_scores, scores)
print(max_scores)