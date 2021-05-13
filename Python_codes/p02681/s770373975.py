s = input()
t = input()

if (t.find(s) == 0) & (len(t) - len(s) == 1):
  print('Yes')
else:
  print('No')