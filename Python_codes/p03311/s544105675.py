import numpy as np
n = int(input())
a = np.fromstring(input(), dtype=np.int64, sep=' ')
for i in range(n):
    a[i] = a[i] - i - 1
x = int(np.median(a))
r = 0
for i in range(n):
    r += abs(a[i]-x)
print(r)