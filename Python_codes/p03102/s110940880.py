import numpy as np

n, m, c = map(int, input().split())
b = np.array([int(i) for i in input().split()])
a = np.array([[int(i) for i in input().split()] for _ in range(n)])

res = 0
for aa in a:
    if np.sum(aa*b)+c > 0:
        res += 1
print(res)
