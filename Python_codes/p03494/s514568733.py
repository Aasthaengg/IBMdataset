import numpy as np
                                              
N = int(input())
A = np.array(list(map(int, input().split())))
i = 0
while True:
    if np.any(A % 2 == 1):
        break
    A = A / 2
    i += 1
print(i)