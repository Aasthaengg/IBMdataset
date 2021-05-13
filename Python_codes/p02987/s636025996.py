s = input()
a1 = s[0]
a2 = s[1]
a3 = s[2]
a4 = s[3]
alis = set()
alis.add(a1)
alis.add(a2)
alis.add(a3)
alis.add(a4)
if len(alis) == 2 and ((a1 == a2 and a3 == a4) or (a1 == a3 and a2 == a4) or (a1 == a4 and a2 == a3)):
  print('Yes')
else:
  print('No')