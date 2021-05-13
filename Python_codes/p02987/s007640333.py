I = input()
S = []
for i in range(4):
  S.append(I[i])

import collections
s = collections.Counter(S)

if s.most_common()[0][1] == 2 and s.most_common()[1][1] == 2:
  print("Yes")
else:
  print("No")