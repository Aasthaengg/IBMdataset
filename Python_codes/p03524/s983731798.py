from collections import Counter
s = input()
d = Counter(s)
n = len(s)
if n%3==0:
  if all(v==n//3 for v in d.values()):
    print('YES')
  else:
    print('NO')
else:
  if all(v==n//3 or v==n//3+1 for v in d.values()):
    print('YES')
  else:
    print('NO')