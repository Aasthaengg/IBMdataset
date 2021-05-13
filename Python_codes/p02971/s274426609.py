import numpy as np
n = int(input())
a = np.array([int(input()) for _ in range(n)])
a1n = a.argmax()
a_s = sorted(a)
a1 = a_s[-1]
a2 = a_s[-2]
for i in range(n):
    if i == a1n:
        print(a2)
    else:
        print(a1)