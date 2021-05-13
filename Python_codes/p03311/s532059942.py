import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
a = [v - i - 1 for i, v in enumerate(a)]
b = sorted(a)[n // 2]
print(np.sum([abs(a - b)]))