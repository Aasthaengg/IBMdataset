import numpy as np

n, m, c = list(map(int, input().split()))
b = np.matrix(list(map(int, input().split())))
a = np.matrix([list(map(int, input().split())) for i in range(n)])
res = int(sum([i > 0 for i in a * b.T + c])[0, 0])
print(res)
