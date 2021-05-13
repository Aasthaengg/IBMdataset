import numpy as np
A = np.array(list(map(int, open(0).read().split())))

next_time = (np.array(A) + 9) // 10 * 10
 
if A[np.nonzero(A%10)].size > 0:
    print(sum(next_time) - (10 - min(A[np.nonzero(A%10)]%10)))
else:
    print(sum(next_time))