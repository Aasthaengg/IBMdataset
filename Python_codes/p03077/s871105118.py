import math
import numpy as np
N,*T = map(int,open(0).read().split())

X = np.array(T).min()

print(4+math.ceil(N/float(X)))
