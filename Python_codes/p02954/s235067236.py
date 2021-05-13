s=input()

logk = (10**100).bit_length()
lens = len(s)
logs = lens.bit_length()
doubling = [[0]*lens for _ in range(logk)]

for i in range(lens):
  if s[i] == 'R':
    doubling[0][i] = i + 1
  else:
    doubling[0][i] = i - 1

for i in range(1,logk):
  for j in range(lens):
    doubling[i][j] = doubling[i-1][doubling[i-1][j]]

from collections import Counter
result = Counter(doubling[logk-1])
for i in range(lens):
  print(result[i])
