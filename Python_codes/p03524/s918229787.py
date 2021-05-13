from collections import Counter
S = input()

dic = Counter(S)

if abs(dic['a']-dic['b']) > 1 or abs(dic['c']-dic['b']) > 1 or abs(dic['a']-dic['c']) > 1:
  print('NO')
else:
  print('YES')