import numpy as np
a, b = map(int, input().split())
c, d = map(int, input().split())
x = (np.array([a, b]) - np.array([c, d]))
print(x[0]*x[1])