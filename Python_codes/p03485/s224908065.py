import numpy as np
ab = input().split(" ")
print(int(np.ceil(np.mean([int(ab[0]), int(ab[1])]))))