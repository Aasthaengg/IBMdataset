import numpy as np
def func(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]
n = int(input())
a = list(map(int, input().split()))
print(a.index(func(a, sum(a) / n)))