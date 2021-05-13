import numpy as np
(n,), *aaa = [list(map(int, s.split())) for s in open(0)]

aaa = np.array(aaa, dtype='int')

cost = np.stack([np.cumsum(aaa[0]), np.zeros(n, dtype='int')])
cost[1][0] = aaa[0][0] + aaa[1][0]

for i in range(1, n):
    cost[1][i] = max(cost[1][i-1], cost[0][i]) + aaa[1][i]

print(cost[-1][-1])