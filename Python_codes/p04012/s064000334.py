from collections import Counter
S = Counter(input())
flag = True
for c in S.values():
  if c % 2 == 1:
    flag = False
if flag:
  print('Yes')
else:
  print('No')
