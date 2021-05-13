import numpy as np
from copy import deepcopy


S = np.array([s for s in input()], str)
T = np.array([t for t in input()], str)
nS, nT = map(len, (S, T))
ans = ''
idx = []

if nS < nT:
    ans = 'UNRESTORABLE'
else:
    for i in range(nS - nT + 1):
        s = S[i:i + nT]
        if np.all((s == T) | (s == '?')):
            idx.append(i)

if not idx:
    ans = 'UNRESTORABLE'
else:
    i = idx[-1]
    S[i:i + nT] = T
    ans = np.where(S == '?', 'a', S)

print(''.join(ans))