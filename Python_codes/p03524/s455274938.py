S = input()
C = [S.count('a'),S.count('b'),S.count('c')]
if len(S) == 1:
  print('YES')
elif len(set(S)) == 1 or max(C)-min(C) > 1:
  print('NO')
else:
  print('YES')