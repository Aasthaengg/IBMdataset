import numpy as np
h, w, k, *s = open(0).read().split()
count, t = 1, np.array([list(s[i]) for i in range(int(h))], dtype=np.object)
for i, j in zip(*np.where(t=='#')):
    t[i][j], count = count, count+1
t = np.where(t=='.', 0, t)
ufill = np.frompyfunc(lambda a, b: a if b == 0 else b, 2, 1)
t = ufill.accumulate(t, dtype=np.object, axis=1)
t = ufill.accumulate(t[:,::-1], dtype=np.object, axis=1)[:,::-1]
t = ufill.accumulate(t, dtype=np.object, axis=0)
t = ufill.accumulate(t[::-1,:], dtype=np.object, axis=0)[::-1,:]
for i in range(int(h)):
    print(*t[i])