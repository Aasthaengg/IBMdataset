import numpy as np
S = np.array(list(map(str, input().rstrip())))
T = np.array(list(map(str, input().rstrip())))
print(sum(S==T))