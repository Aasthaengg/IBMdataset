N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

import collections

cS = collections.Counter(S)
cT = collections.Counter(T)
ans = 0

for x in list(cS.keys()):
  ans = max(cS[x] - cT[x],ans)
print(ans)