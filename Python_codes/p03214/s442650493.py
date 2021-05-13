import numpy as np
n = int(input())
a = list(map(int,input().split()))
nn = list(range(n))
ann = [a,nn]
h = sum(a) / len(a)
idx = np.abs(np.asarray(a) - h).argmin()
print(idx)