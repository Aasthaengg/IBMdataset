K = int(input())
k = K//50
r = K%50
import numpy as np
a = np.arange(50)
x,y = a[50-r:].copy(),a[:50-r].copy()
a[:r] = x+1
a[r:] = y
a += k
print(50)
print(*a)
