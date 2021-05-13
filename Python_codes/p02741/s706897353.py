k=int(input())
import numpy as np
data="1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"

output2 = np.array(data.split(","), dtype = np.int).tolist()

print(output2[k-1])
