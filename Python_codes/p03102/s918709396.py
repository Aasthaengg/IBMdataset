import numpy as np
n, m, c = map(int, input().split())
B = np.array(list(map(int, input().split())))

count = 0
for i in range(n):
    A = np.array(list(map(int, input().split())))
    if np.sum(A * B) + c > 0:
        count += 1
print(count)