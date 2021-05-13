from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
s = set(a)
c = Counter(a)

if n%3 != 0:
  if s == {0}:
    print('Yes')
  else:
    print('No')
else:
  if len(c) > 3:
      print('No')
  elif len(c) == 3:
    a,b,q = list(s)
    if a^b == q and c[a] == n//3 and c[b] == c[q]:
      print('Yes')
    else:
      print('No')
  elif len(c) == 2:
    if not 0 in s:
      print('No')
    else:
      if c[0] == n//3:
        print('Yes')
      else:
        print('No')
  elif len(c) == 1:
    if s == {0}:
      print('Yes')
    else:
      print('No')