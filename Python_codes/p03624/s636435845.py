S = input()
alp = list('abcdefghijklmnopqrstuvwxyz')
for i in range(len(S)):
  if S[i] in alp:
    alp.remove(S[i])
if len(alp) == 0:
  print('None')
else:
  print(alp[0])