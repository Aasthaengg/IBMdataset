import numpy as np
s = int(input())
a = np.full(1000001,-1)
a[0] = s
for i in range(1,1000001):
    if a[i-1] % 2 == 0:
        a[i] = a[i-1] // 2
    elif a[i-1] % 2 != 0:
        a[i] = 3*a[i-1] + 1
    
    if a[i] in set(a[:i-1]):
        print(i+1)
        break
