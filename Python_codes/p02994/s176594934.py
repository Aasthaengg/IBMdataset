import numpy as np
n,l = list(map(int, input().split())) 
t_list = np.array([l+(x+1)-1 for x in range(n)])
flags = [True]*n
idx = np.argmin(np.abs(t_list))
flags[idx] = False
print(np.sum(t_list[flags]))