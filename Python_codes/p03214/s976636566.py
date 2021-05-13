import numpy as np

N = int(input())
a = np.array(list(map(int, input().split())))

a = abs(a - a.mean())

print(a.argmin())
