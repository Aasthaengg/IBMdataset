import numpy as np
import itertools
N, M = map(int, input().split())
x = [0] * N
y = [0] * N
z = [0] * N
for i in range(N):
    x[i], y[i], z[i] = map(int, input().split())

x = np.array(x)
y = np.array(y)
z = np.array(z)

ans = 0
vals = []
for op1,op2,op3 in itertools.product([-1,1],repeat=3):
    #print(op1,op2,op3)
    s = x*op1 + y*op2 + z*op3
    #print(s)
    s.sort()
    vals.append(s[N-M:].sum())


print(max(vals))