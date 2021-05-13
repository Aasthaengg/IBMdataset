import numpy as np
N = int(input())
alist = np.array(list(map(int, input().split())))
mean = sum(alist) / N
alist = np.abs(alist - mean)
print(np.argmin(alist))
