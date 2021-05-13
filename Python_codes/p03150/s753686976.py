import itertools

S = list(input())
KEY = list('keyence')
LK = len(KEY)
L = len(S)
ok = False
for s,t in itertools.combinations(range(L),2):
  idx = 0
  sub_S = S[0:s] + S[t:]
  if sub_S == KEY:
    ok = True
    
if ok or S == KEY:
  print('YES')
else:
  print('NO')
