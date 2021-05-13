import numpy as np
n = int(input())
T = [int(input()) for i in range(n)]

print(np.lcm.reduce(T))
