A = list(map(int, open(0).read().split()))

import numpy as np

if len([(x%10, i) for i,x in enumerate(A) if x%10!=0]) == 0:
    print(sum(A))
else:
    last_order = A[min([(x%10, i) for i,x in enumerate(A) if x%10!=0])[1]]
    print(sum(A) + sum(10 - np.array([x%10 for x in A if x%10!=0])) - (10 - min([x%10 for x in A if x%10!=0])))