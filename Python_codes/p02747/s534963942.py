S = str(input())
S_size = len(S)
hi_size = S.count('hi')
if S_size == hi_size * 2:
  print('Yes')
else:
  print('No')