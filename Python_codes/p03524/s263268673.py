from collections import Counter

S = input()
CNT = Counter(S)

a,b,c = CNT['a'],CNT['b'],CNT['c']

if max(a,b,c) - min(a,b,c) <= 1:
  print('YES')
else:
  print('NO')
