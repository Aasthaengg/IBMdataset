import numpy as np
for i in range(int(input()), 0, -1):
	if np.sqrt(i) == int(np.sqrt(i)):
		print(i)
		exit()