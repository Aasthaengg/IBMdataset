from collections import Counter

S = input()
counter = Counter(S)
if counter['x'] <= 7:
  print('YES')
else:
  print('NO')