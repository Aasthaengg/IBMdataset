import numpy as np
S = np.array(list(map(str, input().rstrip())))

S[np.where(S=="W")] = 1
S[np.where(S=="B")] = 0
S = S.astype(int)
now = np.where(S==1)[0]
goal = np.arange(now.shape[0])

print((now - goal).sum())