s = input()

import numpy as np
B = []
W = []
for i in range(len(s)):
    if s[i] == "B":
        B.append(i)
    elif s[i] == "W":
        W.append(i)

print(sum(np.array(W) - np.array([i for i in range(len(W))])))