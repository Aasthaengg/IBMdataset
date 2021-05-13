import numpy as np
N, T = map(int, input().split())
t = np.array(tuple(map(int, input().split())))
s = t[1:]-t[:-1]-T
S = int(sum(s[s < 0]))
print(N*T+S)