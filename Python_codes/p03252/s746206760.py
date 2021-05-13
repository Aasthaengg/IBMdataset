
from collections import defaultdict

S = input()
T = input()
N = len(S)

SD = defaultdict(set)
TD = defaultdict(set)

for i in range(N):
  SD[S[i]].add(T[i])
  TD[T[i]].add(S[i])

cnt = 0

for i in SD.values():
  cnt = max(cnt, len(i))

for i in TD.values():
  cnt = max(cnt, len(i))

if cnt >= 2:
  print("No")
else:
  print("Yes")