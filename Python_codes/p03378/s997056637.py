N, M, X = map(int, input().split())
A = list(map(int, input().split()))

import numpy as np
A_np = np.array(A)

cost_R = sum(X < A_np)
cost_L = sum(X > A_np)

print(min(cost_R, cost_L))