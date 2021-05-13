from collections import Counter
S = [i for i in str(input())]
c = Counter(S)
m = c.most_common()

n = len(S) // 3
if len(S) == 1:
  print('YES')
elif len(S) == 2:
  if len(m) == 2:
    print('YES')
  else:
    print('NO')
elif len(m) < 3:
  print('NO')
else:
  if len(S) % 3 == 0:
    if (m[0][1]==n) and (m[1][1]==n) and (m[2][1]==n):
      print('YES')
    else:
      print('NO')
  elif len(S) % 3 == 1:
    if (m[0][1]==n+1) and (m[1][1]==n) and (m[2][1]==n):
      print('YES')
    else:
      print('NO')
  else:
    if (m[0][1]==n+1) and (m[1][1]==n+1) and (m[2][1]==n):
      print('YES')
    else:
      print('NO')