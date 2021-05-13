S = input()
T = input()
s = len(S)
t = len(T)
if s+1 == t and S == T[:s]:
  print('Yes')
else:
  print('No')