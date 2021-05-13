import numpy as np
N, C, *L = map(int, open(0).read().split())
program = np.zeros((10**5+2,C+1),np.int32)
for s,t,c in zip(*[iter(L)]*3):
  program[s][c] += 1
  program[t+1][c] += -1
program = np.cumsum(program, axis=0)
ans = max(np.count_nonzero(a) for a in program)
print(ans)