import numpy as np

S = input()
ss = set(S) 
mx = len(S)
for s in ss:
    m = [i for i, si in enumerate(S) if si == s ]
    m.insert(0, -1)
    m.append(len(S))
    mx = min(mx, max(np.diff(m)-1))

print(mx)