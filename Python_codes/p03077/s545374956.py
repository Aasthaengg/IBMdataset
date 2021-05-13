N, *A = map(int, open(0).read().split())

bottleneck = min(A)

import math
print(math.ceil(N / bottleneck) + 4)