N, K = map(int, input().split())
h = list(map(int, input().split()))

import numpy as np
h = np.array(h)

print(len(h[h>=K]))