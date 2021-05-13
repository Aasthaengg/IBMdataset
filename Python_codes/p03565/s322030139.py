import numpy as np

S = input()
T = input()

m = len(S)
n = len(T)
for i in range(m-n, -1, -1):
  if np.prod([s in [t, '?'] for s, t in zip(S[i:i+m], T)]):
    ans = S[:i] + T + S[i+n:]
    ans = ans.replace('?', 'a')
    break
else:
  ans = 'UNRESTORABLE'
print(ans)