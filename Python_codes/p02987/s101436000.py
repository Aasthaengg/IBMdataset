from collections import Counter
s = input()
c = Counter(s)
uni = set(s)
if len(uni) == 2 and c[s[0]] == 2:
  print("Yes")
else:
  print("No")