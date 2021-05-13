N, K = map(int, input().split())
d = list(map(int, input().split()))

import numpy as np

D = np.array(d)

print(len(D[D>=K]))