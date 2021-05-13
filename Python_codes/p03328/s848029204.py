import numpy as np
a, b = map(int, input().split())

num = [i+1 for i in range(999)]

tower = np.cumsum(num)

for j in range(len(tower) - 1):
    if tower[j] - a == tower[j+1] - b:
        print(tower[j] - a)
        break
    else:
        continue