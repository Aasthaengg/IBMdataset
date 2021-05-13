import numpy as np
N = int(input())
x = list(map(int,input().split()))
x.sort()
x_cm = np.cumsum(x)[::-1]
x = x[::-1]
count = 1
for i in range(N-1):
    if x[i]<=x_cm[i+1]*2:
        count += 1
    else:
        break

print(count)