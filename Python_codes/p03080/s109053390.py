import numpy as np
N = int(input())
S = np.sum(np.array([i for i in input()],dtype = 'str') == "R")
print("Yes") if N < S*2 else print("No")