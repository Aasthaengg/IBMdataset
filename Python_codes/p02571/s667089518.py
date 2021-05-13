S = input()
T = input()

import math
res = math.inf

from collections import Counter

mt = list(map(ord, list(T)))
for i in range(len(S) - len(T) + 1):
    # print(S[i: i + len(T)], [a - b for a, b in zip(map(ord, list(S[i: i + len(T)])), mt)])
    res = min(res, len(T) - Counter([a - b for a, b in zip(map(ord, list(S[i: i + len(T)])), mt)])[0])
print(res)