import numpy as np

n, m = map(int, input().split())
res = np.ones(m, dtype=np.int8)
for _ in range(n):
    a_like = np.zeros_like(res)
    for a in map(lambda x: int(x)-1, input()[2:].split()):
        a_like[a] = 1
    res *= a_like
print(np.count_nonzero(res))
