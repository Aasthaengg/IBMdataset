import numpy as np
abc = np.array(list(map(int, input().split())))
key, cnt = np.unique(abc, return_counts=True)
print('Yes' if key.size == 2 else 'No')
