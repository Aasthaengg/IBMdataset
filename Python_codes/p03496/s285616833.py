import numpy as np
N = int(input())
seq = np.array(list(map(int, input().split())))

M, m, x, y = seq.max(), seq.min(), seq.argmax(), seq.argmin()
print(2 * N - 1)
if M + m >= 0:
    for i in range(N):
        print(x + 1, i + 1)
    for i in range(N - 1):
        print(i + 1, i + 2)
else:
    for i in range(N):
        print(y + 1, i + 1)
    for i in range(N - 1, 0, -1):
        print(i + 1, i)
