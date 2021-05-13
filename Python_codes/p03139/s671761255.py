import numpy as np
x = np.array(input().split(' '), int)
print(x[1:].min(),' ', 0 if x[0] >= x[1:].sum() else x[1:].sum() - x[0])