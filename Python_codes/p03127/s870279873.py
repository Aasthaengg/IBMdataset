import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
d = a.min()
while True:
    a1 = a % d
    if all(a1 == 0):
        ans = d
        break
    d = min(a1[a1 != 0])    
print(ans)